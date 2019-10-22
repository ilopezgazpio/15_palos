import numpy as np

# update rule: V(s) = V(s) + alpha * (V(s') - V(s)), being S' the next state

# Use the epsilon-greedy policy:
#   action|s = argmax[over all actions possible from state s]{ V(s) }  if rand > epsilon
#   action|s = select random action from possible actions from state s if rand < epsilon

class Agent:
    def __init__(self, eps, alpha):
        self.eps = eps
        self.alpha = alpha
        self.verbose = False
        self.state_history = []
        self.player = None
        self.V = None

    def setV(self, V):
        self.V = V

    def saveAgentValues(self, path):
        np.savetxt(path, self.V, delimiter="\n", fmt="%s")

    def loadAgentValues(self, path):
        self.V = np.loadtxt(path,delimiter="\n")

    def setEpsilon(self, e):
        self.eps = e

    def decayEpsilon(self, ratio, iterations):
        self.setEpsilon(self.eps - (self.eps / iterations * ratio))

    def set_player1(self):
        self.player = 1

    def set_player2(self):
        self.player = 2

    def set_verbose(self, v):
        self.verbose = v

    def reset_history(self):
        self.state_history = []

    def take_action(self, env):
        r = np.random.rand()
        best_state = None

        if r < self.eps:
            # Take random action
            if self.verbose:
                print("Taking a random action")

            possible_moves = env.possible_moves()
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]
        else:
            # choose the best action based on current values of states V(s)
            move2value = {}  # for debugging
            next_move = None
            best_value = -1

            for m in env.possible_moves():
                env.make_move(m)
                state = env.get_state()
                env.unmake_move(m)
                move2value[m] = self.V[state]
                if self.V[state] > best_value:
                    best_value = self.V[state]
                    best_state = state
                    next_move = m

            if self.verbose:
                env.draw_board()

                print("===========")
                print("IA Movement")
                print("{}, value {}".format(next_move, move2value[next_move]))
                print("===========")
                '''
                for m in move2value.keys():                    
                    if m != next_move:
                        print("Movement {}, value {}".format(m, move2value[m]))
                    else:
                        print("Best movement {}, value {}".format(m, move2value[m]))
                '''

        env.make_move(next_move)

    def update_state_history(self, s):
        self.state_history.append(s)

    def update(self, reward):

        #print("Player: {}, state: {} , reward: {}".format(self.player, self.state_history, reward))

        # BACKTRACK over the states when episode terminates
        for current in reversed(self.state_history):
            # Save reward value for next iteration
            reward = self.V[current] + self.alpha * (reward - self.V[current])
            self.V[current] = reward

        self.reset_history()
