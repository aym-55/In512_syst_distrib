from scripts import *
from scripts.my_constants import *
from random import randint

from strategies import strategy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Mode menu -> menu\n Mode connection -> connection", type=str, default="menu")
parser.add_argument("-i", "--server_ip", help="Ip address of the server", type=str, default="localhost")
args = parser.parse_args()
agent = Agent(args.server_ip)

try:
    if args.mode=="menu" :
        while True:
            cmds = {"header": int(input("0 <-> Broadcast msg\n1 <-> Get data\n2 <-> Move\n3 <-> Get nb connected agents\n4 <-> Get nb agents\n5 <-> Get item owner\n6 <-> Developper\n"))}

            """
            +------------------------------------------+
            | This section is the Developper tool part |
            +------------------------------------------+
            """
            if cmds["header"] == 6:
                dev_input = int(input(f"\t0 <-> Controller\n\t1 <-> Strategy 1\n\t2 <-> Go to point\n\t3 <-> Show map\n"))
                if dev_input == 0:
                    ''' Call the manual controller '''
                    agent.controller()

                elif dev_input == 1:
                    ''' Call the Strategy 1 '''
                    strategy(agent).strat1()

                elif dev_input == 2:
                    ''' Set a point to reach '''
                    dev_x_coord = int(input("X : "))
                    dev_y_coord = int(input("Y : "))
                    agent.go_to_point((dev_x_coord, dev_y_coord))

                elif dev_input == 3:
                    ''' Show pyplot heat map '''
                    agent.show_map()

                continue

            if cmds["header"] == BROADCAST_MSG:
                cmds["Msg type"] = int(input("\t1 <-> Key discovered\n\t2 <-> Box discovered\n\t3 <-> Completed\n"))
                cmds["position"] = agent.get_position()
                cmds["owner"] = randint(0,3) # TODO: specify the owner of the item

            elif cmds["header"] == MOVE:
                cmds["direction"] = int(input("\t0 <-> Stand\n\t1 <-> Left\n\t2 <-> Right\n\t3 <-> Up\n\t4 <-> Down\n\t5 <-> UL\n\t6 <-> UR\n\t7 <-> DL\n\t8 <-> DR\n"))

            agent.network.send(cmds)
    elif args.mode=="connection":
        print("Connecting agent")
        
except KeyboardInterrupt:
    pass