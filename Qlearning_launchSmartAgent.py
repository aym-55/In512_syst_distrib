from scripts import *
from scripts.my_constants import *
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
from threading import Thread

def launch_qtable(path_qtable):
    '''
    path_qtable has to refer to a decision map within the folder "results".
    path_qtable will then import a .npy file
    '''
    Q           = np.load(path_qtable)
    action_max  = np.argmax(Q, axis=0)
    actions     = {0:UP, 1:DOWN, 3:LEFT, 2:RIGHT}
    actions_str = {0:"UP", 1:"DOWN", 2:"RIGHT", 3:'LEFT'}
    agent       = Agent("localhost")

    # Intialize a first move
    agent.move(LEFT)
    agent.move(RIGHT)

    time.sleep(3)

    while agent.get_cell() != 1:
        x, y = agent.get_position()

        # Get the action on the decision map
        action = action_max[y, x] 
        print(f'\nX is {x} Y is {y}')
        print(action)
        print(f' > ACTION {actions_str[action]}')

        agent.move(actions[action])

    input("Done ! [Press ENTER]")

if __name__ == '__main__':

    launch_qtable("results/Qlearning_scsfRandom/scsfRandom_100000.npy")
