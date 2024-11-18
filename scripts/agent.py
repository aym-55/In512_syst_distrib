__author__ = "Aybuke Ozturk Suri, Johvany Gustave"
__copyright__ = "Copyright 2023, IN512, IPSA 2024"
__credits__ = ["Aybuke Ozturk Suri", "Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

from network import Network
from my_constants import *

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
        self.map = np.full((self.w, self.h), np.nan)
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
        try :
            self.network.send({"header":GET_DATA})
            self.msg_cb
            self.map[self.y, self.x] = self.msg["cell_val"]
        except Exception as e:
            print(f'Map not updated : {e}')
        return 0

    def show_map(self):
        print(self.map)
        plt.imshow(self.map, cmap='Reds', interpolation='none')
        plt.colorbar(label='Value')

        plt.title('Matrix with NaN Values')
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        plt.show()

        return 0
    
    def controller(self):
        print("Opening controls...")
        control_command = {"header":MOVE}
        while True:
            print("in the loop")
            data = input("")
            
            if data == "x":
                print("EXITING Controller...")
                return
            elif data == "z":
                print("Going UP")
                control_command["direction"] = UP
            elif data == "q":
                print("Going LEFT")
                control_command["direction"] = LEFT
            elif data == "s":
                print("Going DOWN")
                control_command["direction"] = DOWN
            elif data == "d":
                print("Going RIGHT")
                control_command["direction"] = RIGHT
            
            agent.network.send(control_command)
            self.update_map()

    def strat1(self):
        control_command = {"header":MOVE}

        detection_range = 3
        h_direction = self.h - detection_range

        while self.x != self.w-1:

            while self.y != h_direction:
                if h_direction == self.h - detection_range:
                    control_command["direction"] = DOWN
                elif h_direction == detection_range:
                    control_command["direction"] = UP
                agent.network.send(control_command)
                sleep(0.1)
                self.update_map()
            
            for i in range(5):
                control_command["direction"] = RIGHT
                agent.network.send(control_command)
                sleep(0.1)
                self.update_map()
            
            if self.y == self.h-detection_range:
                h_direction = detection_range
            elif self.y == detection_range:
                h_direction = self.h - detection_range
            

    def go_to_point(self, coord):
        x_goal = coord[0]-1
        y_goal = coord[1]

        if (x_goal < 0 and x_goal > self.h) and (y_goal < 0 and y_goal > self.w):
            print(f'Point ({x_goal}, {y_goal}) is out of bound !\nExiting...')
            return 1

        else : 
            print(f'Going to point ({x_goal}, {y_goal})')

            if x_goal < self.x :
                x_direction = LEFT
            else:
                x_direction = RIGHT

            if y_goal < self.y :
                y_direction = UP
            else:
                y_direction = DOWN

            control_command = {"header":MOVE}

            while True:
                if x_goal == self.x :
                    x_direction = STAND
                else:
                    control_command['direction'] = x_direction
                    agent.network.send(control_command)
                    sleep(0.1)
                    self.update_map()

                if y_goal == self.y :
                    y_direction = STAND
                else:
                    control_command['direction'] = y_direction
                    agent.network.send(control_command)
                    sleep(0.1)
                    self.update_map()

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
            cmds = {"header": int(input("0 <-> Broadcast msg\n1 <-> Get data\n2 <-> Move\n3 <-> Get nb connected agents\n4 <-> Get nb agents\n5 <-> Get item owner\n6 <-> Developper\n"))}
            
            if cmds["header"] == 6:
                dev_input = int(input("\t0 <-> Controller\n\t1 <-> Strategy 1\n\t2 <-> Go to point\n\t3 <-> Show map\n"))
                if dev_input == 0:
                    agent.controller()
                elif dev_input == 1:
                    agent.strat1()
                elif dev_input == 2:
                    dev_x_coord = int(input("X : "))
                    dev_y_coord = int(input("Y : "))
                    agent.go_to_point((dev_x_coord, dev_y_coord))
                elif dev_input == 3:
                    agent.show_map()

                continue

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



