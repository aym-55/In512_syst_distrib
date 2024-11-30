from scripts import *
from scripts.my_constants import *
from threading import Thread
import subprocess
import sys

import numpy as np
import random
import time
import os

class Qlearning:

    def __init__(self):

        ''' Connection to the map to get the informations '''
        self.thread_get_map = Thread(target=self.get_map, daemon=True).start()
        self.map_real       = Server(("localhost", 5555), 1, 3).game.map_real

        ''' Setting up the movement values '''
        self.actions     = {"LEFT":0, "RIGHT":1, "DOWN":2, "UP":3}
        self.actions_str = {0:"LEFT", 1:"RIGHT", 2:"DOWN", 3:'UP'}

    def get_map(self):
        ''' Connecting one agent to the server to get the map '''
        agent_connected = False
        while not agent_connected:
            ''' While agent is not connected retry '''
            try :
                agent           = subprocess.Popen(["python3", "start_agent.py","-m","connection"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                agent_connected = True

            except:
                agent_connected = False

        time.sleep(3) # Let the time to the agent to connect
        agent.terminate()

        return

    def loading_bar(self, end):

        progress        = (self.episode + 1) / end
        bar_length      = 40
        filled_length   = int(bar_length * progress)

        bar = '=' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write(f"\r[{bar}] {progress * 100:.0f}% (ep {self.episode:.0f}/{end:.0f})")
        sys.stdout.flush()


    # ================================================================================
    #                                TRAINING METHODS
    # ================================================================================

    def get_latest_training(self, path):

        if not os.path.exists(path):
            os.mkdir(path)

        ''' Looking for the latest training file to carry on training '''
        list_ext = []
        list_episode = os.listdir(path)

        for f in list_episode: # Checking up the files extensions
            root, ext = os.path.splitext(path+f)
            list_ext.append(ext)

        if ".npy" not in list_ext:
            ''' If no npy file to load start from scratch '''
            self.Q = np.zeros((4, self.map_real.shape[0], self.map_real.shape[1]))
            self.last_episode = 0
            print(f"\n\nNo old run found starting ({self.last_episode})\n\n")

        else:
            ''' If training file loaded start from this file '''
            self.last_episode = 0
            last_file         = list_episode[0]

            for file in list_episode:
                current_episode = int(file.split("_")[-1][:-4])
                if self.last_episode < current_episode:
                    last_file    = file
                    self.last_episode = current_episode

            print(f"\n\nOld run found ({self.last_episode})\n\n")
            self.Q = np.load(path+last_file)


        ''' Training settings '''
        self.alpha           = 0.1  # Global learning rate
        self.gamma           = 0.9  # Reward rate
        self.epsilon_decay   = 0.99 # Episode rate


    def get_action(self,state, action):
        '''
        -------------------------------------------------------------------------------------
        This is the reward function that will use t+1 to get the good reward :
            Considering the current state and the next action we will give the next state,
            reward and if the episode is done
        -------------------------------------------------------------------------------------
        '''
        x, y            = state
        x_next, y_next  = state
        done            = False

        if   action == self.actions["LEFT"]:
            ''' If agent go left take care of the left border '''
            x -= 1
            if 0 > x:
                x_next = 0

            else:
                x_next = x

        elif action == self.actions["RIGHT"]:
            ''' If agent go right take care of the right border '''
            x += 1
            if self.map_real.shape[0]-1 < x:
                x_next = self.map_real.shape[0] - 1

            else:
                x_next = x

        elif action == self.actions["UP"]:
            ''' If agent go up take care of the upper border '''
            y -= 1
            if 0 > y:
                y_next = 0

            else:
                y_next = y

        elif action == self.actions["DOWN"]:
            ''' If agent go down take care of the down border '''
            y += 1
            if self.map_real.shape[1]-1 < y:
                y_next = self.map_real.shape[1] - 1

            else:
                y_next = y

        ''' Handle the rewards '''
        is_inside_the_map = (y>=0 and y<self.map_real.shape[1]) and (x>=0 and x<self.map_real.shape[0])

        if is_inside_the_map and (self.map_real[x, y] == 1):
            ''' If the agent find a reward +100 '''
            reward = 100

        elif is_inside_the_map and (self.map_real[x, y] != 0) :
            ''' If the agent find a nearby reward cell_valuex10 '''
            reward = self.map_real[x, y]*10

        elif is_inside_the_map and (self.map_real[x, y] == 0):
            ''' If the agent did not find anything reward is -10 '''
            reward = -1

        elif not is_inside_the_map:
            ''' If the agent reach a border it gets punished by -100 '''
            reward = -100

        ''' Handle the reached done state '''
        if reward == 100:
            done = True

        return (x_next, y_next), reward, done


    def traditional_Qlearning(self, n_episode, from_start=False):
        '''
        This is the traditional Qlearning Algorithm :
            It is taking the using the current state and the next one
            to evaluate the better action to do while being on a cell
        '''

        path_traditional = "./results/Qlearning_Traditional/"
        self.get_latest_training(path_traditional)

        if from_start:
            print("Restart Training...")
            self.Q = np.zeros((4, self.map_real.shape[0], self.map_real.shape[1]))
            self.last_episode = 0

        initial_state   = (0, 0)
        epsilon         = 1.0 * (self.last_episode+1)

        for self.episode in range(self.last_episode, n_episode+1):

            self.loading_bar(n_episode)

            state = initial_state
            done  = False

            while not done:

                ''' If the episode rate is too early we will randomly choose to explore better '''
                if random.uniform(0, 1) < epsilon:
                    action = random.choice(list(self.actions.values()))

                else:
                    action = np.argmax(self.Q[:, state[0], state[1]])

                next_state, reward, done = self.get_action(state, action)

                self.Q[action, state[0], state[1]] += self.alpha * (
                    reward + self.gamma * np.max(self.Q[:, next_state[0], next_state[1]]) - self.Q[action, state[0], state[1]]
                )

                state = next_state

            epsilon *= self.epsilon_decay # Increase the episode rate

        np.save(f"{path_traditional}{int(self.episode)}.npy", self.Q)
        input("\n\nDONE ! [Press Enter to terminate]")

    def traditionalRandom_Qlearning(self, n_episode, from_start=False):
        '''
        This is the traditional Qlearning Algorithm Random :
            It is using the same agldorithm than previously except
            every epsiode start at a random position to explore more
            path options.
        '''

        path_traditionalRandom = "./results/Qlearning_TraditionalRandom/"
        self.get_latest_training(path_traditionalRandom)

        if from_start:
            print("Restart Training...")
            self.Q = np.zeros((4, self.map_real.shape[0], self.map_real.shape[1]))
            self.last_episode = 0

        epsilon         = 1.0 * (self.last_episode+1)
        exploration_map = np.zeros(self.map_real.shape)
        state           = (random.randint(0, self.map_real.shape[0]-1), random.randint(0, self.map_real.shape[1]-1))

        for self.episode in range(self.last_episode, n_episode+1):

            self.loading_bar(n_episode)

            # Use the random position unexplored to explore better options
            exploration_map[state[0], state[1]] += 1
            least_explored = np.argwhere(exploration_map == exploration_map.min())
            state = random.choice(least_explored)

            done  = False

            while not done:

                ''' If the episode rate is too early we will randomly choose to explore better '''
                if random.uniform(0, 1) < epsilon:
                    action = random.choice(list(self.actions.values()))

                else:
                    action = np.argmax(self.Q[:, state[0], state[1]])

                next_state, reward, done = self.get_action(state, action)

                self.Q[action, state[0], state[1]] += self.alpha * (
                    reward + self.gamma * np.max(self.Q[:, next_state[0], next_state[1]]) - self.Q[action, state[0], state[1]]
                )

                state = next_state

            epsilon *= self.epsilon_decay # Increase the episode rate

        np.save(f"{path_traditionalRandom}Random_{int(self.episode)}.npy", self.Q)
        input("\n\nDONE ! [Press Enter to terminate]")


if __name__ =='__main__':

    training = Qlearning()
    training.traditionalRandom_Qlearning(100000,from_start=True)
