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

    human = Human()
    rounds = 0

    if args.saveAgentState:
        player1.saveAgentValues(args.path)

    while True:
        print("Starting round {}".format(rounds))

        if rounds % 2 == 0:
            aiPlayer = player1
            aiPlayer.set_verbose(True)
            aiPlayer.eps = 0
            aiPlayer.set_player1()
            human.set_player2()
            env.play_game(aiPlayer, human, draw=2)
        else:
            aiPlayer = player2
            aiPlayer.set_verbose(True)
            aiPlayer.eps = 0
            aiPlayer.set_player2()
            human.set_player1()
            env.play_game(human, aiPlayer, draw=1)

        if env.winner == aiPlayer.player:
            print("\n Game Over \n")
        elif env.winner == human.player:
            print("\n Victory \n")

        rounds += 1

        if sys.version_info[0] >= 3:
            answer = input("Play again? [Y/n]: ")
        else:
            answer = raw_input("Play again? [Y/n]: ")

        if answer and answer.lower()[0] == 'n':
            break

