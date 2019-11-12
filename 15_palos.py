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
