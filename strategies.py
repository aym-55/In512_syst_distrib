
from scripts import *
from scripts.my_constants import *
from scripts.agent import *

class strategy:
    ''' Strategy class use the input agent object to create control sequence '''
    def __init__(self, _agent):
        self.agent       = _agent
        request_nb_agent = {"header":GET_NB_CONNECTED_AGENTS}

        print("Waiting for nb agents...")
        is_nb_missing = True
        while is_nb_missing == True:
            try :
                self.agent.network.send(request_nb_agent)
                self.nb_agent = self.agent.msg["nb_agents"]
                is_nb_missing = False

            except:
                is_nb_missing = True


    def search_key_down(self):
        print("Search Key down")
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
        print("Search Key up")
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
        print("Search Key right")
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
                print("Key found mgl !!!") 
                self.agent.move(DOWN_RIGHT)
                self.agent.move(DOWN_RIGHT)
                ## Condition à completer                                          
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
        print("Search Key left")
        self.agent.move(UP_LEFT)
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
        print("Search Chest down")
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
        print("Search Chest up")
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
        print("Search Chest right")
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
        print("Search Chest left")
        self.agent.move(UP_LEFT)
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
        ''' Strategy 1: Move in a serpentine pattern covering the entire grid '''
        detection_range = 2

        # Set the boundary in the case of 1 agent
        if self.nb_agent == 1:
            self.w_boundary = (0, self.agent.w)
            self.h_boundary = (0, self.agent.h)

        # Set the boundary in the case of 2 agents
        elif self.nb_agent == 2:
            if self.agent.agent_id == 0:
                self.w_boundary = (0, self.agent.w)
                self.h_boundary = (0, int(self.agent.h/2))

            else:
                self.w_boundary = (0, self.agent.w)
                self.h_boundary = (int(self.agent.h/2), self.agent.h)

        # Set the boundary in the case of 3 agents
        elif self.nb_agent == 3:
            if self.agent.agent_id == 0:
                self.w_boundary = (0, int(self.agent.w/2))
                self.h_boundary = (0, int(self.agent.h/2))

            elif self.agent.agent_id == 1:
                self.w_boundary = (int(self.agent.w/2), self.agent.w)
                self.h_boundary = (0, int(self.agent.h/2))

            else:
                self.w_boundary = (0, self.agent.w)
                self.h_boundary = (int(self.agent.h/2), self.agent.h)

        # Set the boundary in the case of 4 agents
        elif self.nb_agent == 4:
            if self.agent.agent_id == 0:
                self.w_boundary = (0, int(self.agent.w/2))
                self.h_boundary = (0, int(self.agent.h/2))

            elif self.agent.agent_id == 1:
                self.w_boundary = (int(self.agent.w/2), self.agent.w)
                self.h_boundary = (0, int(self.agent.h/2))

            elif self.agent.agent_id == 2:
                self.w_boundary = (0, int(self.agent.w/2))
                self.h_boundary = (int(self.agent.h/2), self.agent.h)

            else:
                self.w_boundary = (int(self.agent.w/2), self.agent.w)
                self.h_boundary = (int(self.agent.h/2), self.agent.h)


        # Gives the up and down edges
        up_edge   = self.h_boundary[0] + detection_range
        down_edge = self.h_boundary[1] - detection_range - 1

        # Move to the nearest corner
        if self.agent.x > self.w_boundary[1]/2:
            if self.agent.y > self.h_boundary[1]/2:
                self.agent.go_to_point((self.w_boundary[1]-3,self.h_boundary[1]-3))
                h_direction = up_edge
                w_direction = 'left'
            else:
                self.agent.go_to_point((self.w_boundary[1]-3,self.h_boundary[0]+2))
                h_direction = down_edge
                w_direction = 'left'
        else :
            if self.agent.y > self.h_boundary[1]/2:
                self.agent.go_to_point((self.w_boundary[0]+2,self.h_boundary[1]-3))
                h_direction = up_edge
                w_direction = 'right'
            else:
                self.agent.go_to_point((self.w_boundary[0]+2,self.h_boundary[0]+2))
                h_direction = down_edge
                w_direction = 'right'

        while (self.agent.x < self.w_boundary[1]-1) and (self.agent.x > self.w_boundary[0]):
            ''' While none of the boudaries has been reach carry on the process '''

            while self.agent.y != h_direction:
                ''' While the limit is not reach carry on the given y direcion '''
                hist_tile_h = self.agent.get_position() # Save state to get back on track after the research
                if h_direction == down_edge:
                    if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_down()
                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_down()
                    if hist_tile_h[1] > down_edge:
                        self.agent.go_to_point((hist_tile_h[0], down_edge))
                    else:
                        self.agent.move(DOWN)
                        
                elif h_direction == up_edge:
                    if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_up()
                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_up()
                    if hist_tile_h[1] < up_edge:
                        self.agent.go_to_point((hist_tile_h[0], up_edge))
                    else:
                        self.agent.move(UP)


            hist_tile_w = self.agent.get_position() # Save state to get back on track after the research
            for i in range(2*detection_range + 1):
                ''' Lateral moves of 5 (the detection limit) '''
                if w_direction == 'right':
                    self.agent.move(RIGHT)
                    if self.agent.msg["cell_val"] == 0.25:
                        hist_tile_w = self.agent.get_position()
                        self.search_key_right()
                        if np.abs(self.agent.get_position()[0]-hist_tile_w[0])>5 :
                            while np.abs(self.agent.get_position()[0]-hist_tile_w[0])!=5:
                                self.agent.move(LEFT)
                        if self.agent.x > self.w_boundary[1]:
                            self.agent.go_to_point((self.w_boundary[1], hist_tile_w[1]))
                        break

                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_right()
                        if np.abs(self.agent.get_position()[0]-hist_tile_w[0])>5 :
                            while np.abs(self.agent.get_position()[0]-hist_tile_w[0])!=5:
                                self.agent.move(LEFT)
                        if self.agent.x > self.w_boundary[1]:
                            self.agent.go_to_point((self.w_boundary[1], hist_tile_w[1]))
                        break

                elif w_direction == 'left':
                    self.agent.move(LEFT)
                    if self.agent.msg["cell_val"] == 0.25:
                        self.search_key_left()
                        if np.abs(self.agent.get_position()[0]-hist_tile_w[0])>5 :
                            while np.abs(self.agent.get_position()[0]-hist_tile_w[0])!=5:
                                self.agent.move(RIGHT)
                        if self.agent.x < self.w_boundary[0]:
                            self.agent.go_to_point((self.w_boundary[0], hist_tile_w[1]))
                        break
                    elif self.agent.msg["cell_val"] == 0.3:
                        self.search_chest_left()
                        if np.abs(self.agent.get_position()[0]-hist_tile_w[0])>5 :
                            while np.abs(self.agent.get_position()[0]-hist_tile_w[0])!=5:
                                self.agent.move(RIGHT)
                        if self.agent.x < self.w_boundary[0]:
                            self.agent.go_to_point((self.w_boundary[0], hist_tile_w[1]))
                        break

            ''' Handle the direction of y '''
            if self.agent.y == down_edge: # Go UP
                h_direction = self.h_boundary[0] + detection_range

            elif self.agent.y == up_edge: # Go DOWN
                h_direction = self.h_boundary[1] - detection_range - 1


if __name__ == '__main__':
    agent_test = Agent("localhost")
    strategy(agent_test).strat1()
