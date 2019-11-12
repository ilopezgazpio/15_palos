from Director import Director
from Scene import Scene
from DummyScene import DummyScene

from Environment import Environment
from Human_Agent import Human
from Agent import Agent

import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
import os.path


'''
Test game
'''

if __name__ == '__main__':

    # todo -> resolution should be an argument
    parser = argparse.ArgumentParser(description='Play the 15 sticks game.')
    parser.add_argument('--alpha', type=float, default=0.05, help='Learning rate value, for the update of state values')
    parser.add_argument('--epsilon', type=float, default=0.15, help='Exploration vs explotation ratio')
    parser.add_argument('--epsilon_decay', type=float, default=1, help='Epsilon decay ratio')
    parser.add_argument('--path', type=str, default="agentVS.txt", help='Path to save/load agent state')
    args = parser.parse_args()

    director = Director()
    director.select_scene('GameScene', args)
    director.project_scene('GameScene')


    '''
    env = Environment()

    aiPlayer = Agent(args.epsilon, args.alpha)
    aiPlayer.loadAgentValues(args.path)
    aiPlayer.eps = 0
    aiPlayer.set_verbose(True)

    human = Human()
    rounds = 0

    while True:
        print("Starting round {}".format(rounds))

        if rounds % 2 == 0:
            aiPlayer.set_player1()
            human.set_player2()
            env.play_game(aiPlayer, human, draw=2)
        else:
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
    '''