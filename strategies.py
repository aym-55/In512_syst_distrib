
from scripts import *
from scripts.my_constants import *
from scripts.agent import *

class strategy:
    ''' Strategy class use the input agent object to create control sequence '''
    def __init__(self, _agent):
        self.agent = _agent

    def search_key_down(self):
        self.agent.move(DOWN_LEFT)
        if self.agent.msg["cell_val"] == 0.5:
            self.agent.move(DOWN_LEFT)
            if self.agent.msg["cell_val"] == 0.25:
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                # Arrivée à la clé
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                self.agent.move(DOWN)
            elif self.agent.msg["cell_val"] == 0.5:
                self.agent.move(RIGHT)
                # Arrivée à la clé
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN)
                self.agent.move(DOWN) 
            else:
                # Arrivée à la clé
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN)                                                
        else:
            self.agent.move(UP_RIGHT)
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée à la clé
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN)
            else:
                self.agent.move(LEFT)
                # Arrivée à la clé
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN)
                self.agent.move(DOWN)

    def search_key_up(self):
        self.agent.move(UP_LEFT)
        if self.agent.msg["cell_val"] == 0.5:
            self.agent.move(UP_LEFT)
            if self.agent.msg["cell_val"] == 0.25:
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                # Arrivée à la clé
                self.agent.move(UP)
                self.agent.move(UP)
                self.agent.move(UP)
            elif self.agent.msg["cell_val"] == 0.5:
                self.agent.move(RIGHT)
                # Arrivée à la clé 
                self.agent.move(UP_RIGHT)
                self.agent.move(UP)
                self.agent.move(UP)
            else:
                # Arrivée à la clé
                self.agent.move(UP_RIGHT)
                self.agent.move(UP_RIGHT)
                self.agent.move(UP)                                           
        else:
            self.agent.move(DOWN_RIGHT)
            self.agent.move(UP_RIGHT)
            self.agent.move(UP_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée à la clé
                self.agent.move(UP_LEFT)
                self.agent.move(UP_LEFT)
                self.agent.move(UP)
            else:
                self.agent.move(LEFT)
                # Arrivée à la clé
                self.agent.move(UP_LEFT)
                self.agent.move(UP)
                self.agent.move(UP)

    def search_key_right(self):
        self.agent.move(UP_RIGHT)
        if self.agent.msg["cell_val"] == 0.5:
            self.agent.move(UP_RIGHT)
            if self.agent.msg["cell_val"] == 0.25:
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                # Arrivée à la clé
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
            elif self.agent.msg["cell_val"] == 0.5:
                self.agent.move(DOWN)
                # Arrivée à la clé 
                self.agent.move(DOWN_RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
            else:
                # Arrivée à la clé
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN_RIGHT)
                self.agent.move(RIGHT)                                             
        else:
            self.agent.move(DOWN_LEFT)
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée à la clé
                self.agent.move(UP_RIGHT)
                self.agent.move(UP_RIGHT)
                self.agent.move(RIGHT)
            else:
                self.agent.move(UP)
                # Arrivée à la clé
                self.agent.move(UP_RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                
    def search_key_left(self):
        self.agent.move(UP_RIGHT)
        if self.agent.msg["cell_val"] == 0.5:
            self.agent.move(UP_LEFT)
            if self.agent.msg["cell_val"] == 0.25:
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                # Arrivée à la clé
                self.agent.move(LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)
            elif self.agent.msg["cell_val"] == 0.5:
                self.agent.move(DOWN)
                # Arrivée à la clé 
                self.agent.move(DOWN_LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)
            else:
                # Arrivée à la clé
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN_LEFT)
                self.agent.move(LEFT)                                             
        else:
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_LEFT)
            self.agent.move(DOWN_LEFT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée à la clé
                self.agent.move(UP_LEFT)
                self.agent.move(UP_LEFT)
                self.agent.move(LEFT)
            else:
                self.agent.move(UP)
                # Arrivée à la clé
                self.agent.move(UP_LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)

    def search_chest_down(self):
        self.agent.move(DOWN_LEFT)
        if self.agent.msg["cell_val"] == 0.6:
            self.agent.move(DOWN_LEFT)
            if self.agent.msg["cell_val"] == 0.3:
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                # Arrivée au coffre
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                self.agent.move(DOWN)
            elif self.agent.msg["cell_val"] == 0.6:
                self.agent.move(RIGHT)
                # Arrivée au coffre
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN)
                self.agent.move(DOWN) 
            else:
                # Arrivée au coffre
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN)                                                
        else:
            self.agent.move(UP_RIGHT)
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée au coffre
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN)
            else:
                self.agent.move(LEFT)
                # Arrivée au coffre
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN)
                self.agent.move(DOWN)

    def search_chest_up(self):
        self.agent.move(UP_LEFT)
        if self.agent.msg["cell_val"] == 0.6:
            self.agent.move(UP_LEFT)
            if self.agent.msg["cell_val"] == 0.3:
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                # Arrivée au coffre
                self.agent.move(UP)
                self.agent.move(UP)
                self.agent.move(UP)
            elif self.agent.msg["cell_val"] == 0.6:
                self.agent.move(RIGHT)
                # Arrivée au coffre 
                self.agent.move(UP_RIGHT)
                self.agent.move(UP)
                self.agent.move(UP)
            else:
                # Arrivée au coffre
                self.agent.move(UP_RIGHT)
                self.agent.move(UP_RIGHT)
                self.agent.move(UP)                                           
        else:
            self.agent.move(DOWN_RIGHT)
            self.agent.move(UP_RIGHT)
            self.agent.move(UP_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée au coffre
                self.agent.move(UP_LEFT)
                self.agent.move(UP_LEFT)
                self.agent.move(UP)
            else:
                self.agent.move(LEFT)
                # Arrivée au coffre
                self.agent.move(UP_LEFT)
                self.agent.move(UP)
                self.agent.move(UP)

    def search_chest_right(self):
        self.agent.move(UP_RIGHT)
        if self.agent.msg["cell_val"] == 0.6:
            self.agent.move(UP_RIGHT)
            if self.agent.msg["cell_val"] == 0.3:
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                # Arrivée au coffre
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
            elif self.agent.msg["cell_val"] == 0.6:
                self.agent.move(DOWN)
                # Arrivée au coffre 
                self.agent.move(DOWN_RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
            else:
                # Arrivée au coffre
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN_RIGHT)
                self.agent.move(RIGHT)                                             
        else:
            self.agent.move(DOWN_LEFT)
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_RIGHT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée au coffre
                self.agent.move(UP_RIGHT)
                self.agent.move(UP_RIGHT)
                self.agent.move(RIGHT)
            else:
                self.agent.move(UP)
                # Arrivée au coffre
                self.agent.move(UP_RIGHT)
                self.agent.move(RIGHT)
                self.agent.move(RIGHT)
                
    def search_chest_left(self):
        self.agent.move(UP_RIGHT)
        if self.agent.msg["cell_val"] == 0.6:
            self.agent.move(UP_LEFT)
            if self.agent.msg["cell_val"] == 0.3:
                self.agent.move(DOWN)
                self.agent.move(DOWN)
                # Arrivée au coffre
                self.agent.move(LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)
            elif self.agent.msg["cell_val"] == 0.6:
                self.agent.move(DOWN)
                # Arrivée au coffre 
                self.agent.move(DOWN_LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)
            else:
                # Arrivée au coffre
                self.agent.move(DOWN_LEFT)
                self.agent.move(DOWN_LEFT)
                self.agent.move(LEFT)                                             
        else:
            self.agent.move(DOWN_RIGHT)
            self.agent.move(DOWN_LEFT)
            self.agent.move(DOWN_LEFT)
            if self.agent.msg["cell_val"] == 1:
                # Arrivée au coffre
                self.agent.move(UP_LEFT)
                self.agent.move(UP_LEFT)
                self.agent.move(LEFT)
            else:
                self.agent.move(UP)
                # Arrivée au coffre
                self.agent.move(UP_LEFT)
                self.agent.move(LEFT)
                self.agent.move(LEFT)

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
                    if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_down()
                        continue
                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_down()
                        continue 
                elif h_direction == up_edge:
                    self.agent.move(UP)
                    if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_up()
                        continue
                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_up()
                        continue
        
            ''' 5 steps on the right cells '''
            for i in range(2*detection_range + 1):
                self.agent.move(RIGHT)
                if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_right()
                        continue
                elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_right()
                        #break
                
                
            
            ''' Handle the direction of y '''
            if self.agent.y == down_edge: # Go UP
                h_direction = detection_range

            elif self.agent.y == up_edge: # Go DOWN
                h_direction = self.agent.h - detection_range - 1


if __name__ == '__main__':
    agent_test = Agent("localhost")
    strategy(agent_test).strat1()
