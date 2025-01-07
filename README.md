# IN512_Project

*authors : A.LEGRAND, T.MONSELLIER, M.VINATIER*

---

Based on the Reinforcement Learning "Qlearning" method our team wanted to build an effective path in between the key and the chest of the map for our agent. In order to do that, a fully completed and eexplored map had to be created. To explore the map, our team decided to attribute areas splitted byn the number of agent on the map. Each agent has its own boundary within they have to find the chests and keys. In their areas, the agent will go like a snake in order to detect point of interest.

---

## Results

The Results folder is where all the Qlearning decision matrices are exported. In order to use one, this is where you can import it.

## Scripts

Script is the folder you can import in your codes to make its classes and methods easier to manipulate.

## Files

### Qlearning

- **Qlearning_Traditional.py** : Is using the common QLearning algorithm to create the decision matrix. This file is used to train the model.

- **Qlearning_SCSF.py** : Is using the State Chain Sequential Feedback method for the QLearning algorithm to create the decision matrix. This file is used to train the model.

- **Qlearning_Table.ipynb** : Is used to perform review of the decision matrices.

- **Qlearning_launchSmartAgent.py** : Is using a given decision matrix to launch an agent using it.

### Strategies file

- **strategies.py** : Is where you will find the different methods that has been assembled to create a strategy.

### Start files

- **start_agent.py** : Is using the agent class to link it with the strategies. Also some usefull function to manipulate the agent are given here.

- **start_server.py** : Launch the server map.