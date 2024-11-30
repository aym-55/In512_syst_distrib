from scripts import *
from scripts.my_constants import *
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
from threading import Thread

def launch_qtable(path_qtable):

    Q           = np.load(path_qtable)
    action_max  = np.argmax(Q, axis=0)
    actions     = {0:UP, 1:DOWN, 3:LEFT, 2:RIGHT}
    actions_str = {0:"UP", 1:"DOWN", 2:"RIGHT", 3:'LEFT'}
    agent       = Agent("localhost")
    """
    sns.heatmap(action_max)
    plt.show(block=True)
    """
    agent.move(LEFT)
    agent.move(RIGHT)

    time.sleep(3)

    while agent.get_cell() != 1:
        x, y = agent.get_position()

        action = action_max[y, x] 
        print(f'\nX is {x} Y is {y}')
        print(action)
        print(f' > ACTION {actions_str[action]}')

        agent.move(actions[action])

    input("Done ! [Press ENTER]")

if __name__ == '__main__':

    launch_qtable("results/Qlearning_TraditionalRandom/Random_100000.npy")
