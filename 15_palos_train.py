from Environment import Environment
from Human_Agent import Human
from Agent import Agent

import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys


'''
Train agent
'''

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate data.')
    parser.add_argument('--episodes', type=int, default=50000, help='Number of episodes to train the model')
    parser.add_argument('--alpha', type=float, default=0.05, help='Learning rate value, for the update of state values')
    parser.add_argument('--epsilon', type=float, default=0.15, help='Exploration vs explotation ratio')
    parser.add_argument('--epsilon_decay', type=float, default=1, help='Epsilon decay ratio')
    parser.add_argument('--saveAgentState', default=True, action='store_true', help='Save trained agent V(s) values')
    parser.add_argument('--path', type=str, default="agentVS.txt", help='Path to save/load agent state')

    args = parser.parse_args()

    env = Environment()

    player1 = Agent(args.epsilon, args.alpha)
    player1.set_player1()
    player1.setV(env.initial_values())

    player2 = Agent(args.epsilon, args.alpha)
    player2.set_player2()
    player2.setV(env.initial_values())

    players = [player1, player2]

    print("=================")
    print("Starting training")
    print("=================")
    for e in range(args.episodes):
        if e % 5000 == 0:
            print(e)
        order = np.random.permutation( range(len(players)) )
        env.play_game( players[order[0]], players[order[1]] )
        [player.decayEpsilon(args.epsilon_decay, args.episodes) for player in players]

    print("============")
    print("End training")
    print("============")

    if args.saveAgentState:
        player1.saveAgentValues(args.path)
    
