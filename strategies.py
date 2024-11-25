
from scripts import *
from scripts.my_constants import *


class strategy:
    ''' Strategy class use the input agent object to create control sequence '''
    def __init__(self, _agent):
        self.agent = _agent

    def strat1(self):
        ''' Strategy 1 aim to move up and down with a lateral movement of detection range size '''
        detection_range = 2
        up_edge         = detection_range
        down_edge       = self.agent.h - detection_range - 1

        h_direction     = down_edge  # Go DOWN
        while self.agent.x != self.agent.w-1:

            while self.agent.y != h_direction:
                ''' While the limit is not reach carry on the given y direcion '''
                if h_direction == down_edge:
                    self.agent.move(DOWN)

                elif h_direction == up_edge:
                    self.agent.move(UP)
        
            ''' 5 steps on the right cells '''
            for i in range(2*detection_range + 1):
                self.agent.move(RIGHT)
            
            ''' Handle the direction of y '''
            if self.agent.y == down_edge: # Go UP
                h_direction = detection_range

            elif self.agent.y == up_edge: # Go DOWN
                h_direction = self.agent.h - detection_range - 1


if __name__ == '__main__':
    agent_test = Agent("localhost")
    strategy(agent_test).strat1()
