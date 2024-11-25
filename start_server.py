from scripts import *
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip_server", help="Ip address of the server", type=str, default="localhost")
parser.add_argument("-nb", "--nb_agents", help="Number of agents: 1, 2, 3 or 4", type=int, default=1)
parser.add_argument("-mi", "--map_id", help="Map to load: 1 or 2 or 3", type=int, default=3)


args = parser.parse_args()
port = 5555

if not args.nb_agents in range(1, 5):    #Game are only designed for 1 to 4 agents
    print("The number of agents should range between 1 and 4!")
    sys.exit()
if not args.map_id in range(1, 4):    #There are only 3 maps
    print("There are only 2 maps!")
    sys.exit()
server = Server((args.ip_server, port), args.nb_agents, args.map_id)