__author__ = "Aybuke Ozturk Suri, Johvany Gustave"
__copyright__ = "Copyright 2023, IN512, IPSA 2024"
__credits__ = ["Aybuke Ozturk Suri", "Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

if __name__ == "__main__":
    from network import Network
    from my_constants import *

else:
    from .network import Network
    from .my_constants import *

from threading import Thread
import numpy as np
from time import sleep

import matplotlib.pyplot as plt

class Agent:
    """ Class that implements the behaviour of each agent based on their perception and communication with other agents """
    def __init__(self, server_ip):
        #TODO: DEINE YOUR ATTRIBUTES HERE

        #DO NOT TOUCH THE FOLLOWING INSTRUCTIONS
        self.network = Network(server_ip=server_ip)
        self.agent_id = self.network.id
        self.running = True
        self.network.send({"header": GET_DATA})
        self.msg = {}
        env_conf = self.network.receive()
        self.nb_agent_expected = 0
        self.nb_agent_connected = 0
        self.x, self.y = env_conf["x"], env_conf["y"]   #initial agent position
        self.w, self.h = env_conf["w"], env_conf["h"]   #environment dimensions
        cell_val = env_conf["cell_val"] #value of the cell the agent is located in
        self.map = np.full((self.h, self.w), np.nan)
        print(cell_val)
        Thread(target=self.msg_cb, daemon=True).start()
        print("hello")
        self.wait_for_connected_agent()

        
    def msg_cb(self): 
        """ Method used to handle incoming messages """
        while self.running:
            msg = self.network.receive()
            self.msg = msg
            if msg["header"] == MOVE:
                self.x, self.y =  msg["x"], msg["y"]
                print(self.x, self.y)
            elif msg["header"] == GET_NB_AGENTS:
                self.nb_agent_expected = msg["nb_agents"]
            elif msg["header"] == GET_NB_CONNECTED_AGENTS:
                self.nb_agent_connected = msg["nb_connected_agents"]

            self.update_map()

            print("hellooo: ", msg)
            print("agent_id ", self.agent_id)
            

    def wait_for_connected_agent(self):
        self.network.send({"header": GET_NB_AGENTS})
        check_conn_agent = True
        while check_conn_agent:
            if self.nb_agent_expected == self.nb_agent_connected:
                print("both connected!")
                check_conn_agent = False

                  

    #TODO: CREATE YOUR METHODS HERE...
    def update_map(self):
        """ Update self.map with cell value """
        try :
            self.map[self.y, self.x] = self.msg["cell_val"] # Extract the cell value
            return 0

        except Exception as e:
            # Sometime value is 31 for axis 1
            print(f'Map not updated : {e}') 
            return 1
        

    def show_map(self):
        """Affiche la carte en utilisant pyplot, mise à jour en temps réel."""
        plt.ion()
        fig, ax = plt.subplots()
        cax = ax.imshow(self.map, cmap='Reds', vmin=0, vmax=1, interpolation='none')
        fig.colorbar(cax, label='Value')

        plt.title('Agent Heatmap')
        plt.xlabel('Y')
        plt.ylabel('X')

        cax.set_data(self.map)  # Update map
        fig.canvas.draw()
        
        plt.show() 
     

    def move(self, direction):
        control_command = {"header":MOVE}           # Set the header frame
        control_command["direction"] = direction    # Set the direction frame
        self.network.send(control_command)          # Send the command
        sleep(0.1)
        return 0


    def controller(self):

        while True:
            data = str(input("")).lower()

            if data == "x":
                ''' EXIT '''
                print("EXITING Controller...")
                return
            
            elif data == "z":
                ''' UP '''
                self.move(UP)

            elif data == "q":
                ''' LEFT '''
                self.move(LEFT)

            elif data == "s":
                ''' DOWN '''
                self.move(DOWN)

            elif data == "d":
                ''' RIGHT '''
                self.move(RIGHT)

    def go_to_point(self, coord):
        ''' Lead the agent to the given tuple coordonates '''
        x_goal = coord[0]-1
        y_goal = coord[1]-1

        if (x_goal < 0 and x_goal > self.h) and (y_goal < 0 and y_goal > self.w):
            ''' Checking the map outbounds '''
            print(f'Point ({x_goal}, {y_goal}) is out of bound !\nExiting...')
            return 1

        else : 
            print(f'Going to point ({x_goal}, {y_goal})')

            ''' Checking for the direction on x '''
            if x_goal <= self.x :
                x_direction = LEFT
            else:
                x_direction = RIGHT

            ''' Checking for the direction on y '''
            if y_goal <= self.y :
                y_direction = UP
            else:
                y_direction = DOWN

            while True:
                ''' Increment step to the given direction (not using diagonal yet) '''
                if x_goal == self.x :      # X goal is reached
                    x_direction = STAND 
                else:
                    self.move(x_direction) # Carry on X

                if y_goal == self.y :      # Y goal is reached
                    y_direction = STAND
                else:
                    self.move(y_direction) # Carry on Y

                ''' Point has been reached by the agent '''
                if y_direction == x_direction:
                    return 0
                

 
if __name__ == "__main__":
    from random import randint
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--server_ip", help="Ip address of the server", type=str, default="localhost")
    args = parser.parse_args()

    agent = Agent(args.server_ip)
    
    try:    #Manual control test0
        while True:
            cmds = {"header": int(input("0 <-> Broadcast msg\n1 <-> Get data\n2 <-> Move\n3 <-> Get nb connected agents\n4 <-> Get nb agents\n5 <-> Get item owner\n"))}
            if cmds["header"] == BROADCAST_MSG:
                cmds["Msg type"] = int(input("\t1 <-> Key discovered\n\t2 <-> Box discovered\n\t3 <-> Completed\n"))
                cmds["position"] = (agent.x, agent.y)
                cmds["owner"] = randint(0,3) # TODO: specify the owner of the item
            elif cmds["header"] == MOVE:
                cmds["direction"] = int(input("\t0 <-> Stand\n\t1 <-> Left\n\t2 <-> Right\n\t3 <-> Up\n\t4 <-> Down\n\t5 <-> UL\n\t6 <-> UR\n\t7 <-> DL\n\t8 <-> DR\n"))
            agent.network.send(cmds)
    except KeyboardInterrupt:
        pass
# it is always the same location of the agent first location



