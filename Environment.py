import numpy as np

class Environment:

    def __init__(self):
        # levels in the game
        self.levels = 3
        # number of pieces per level
        self.length = [3, 5, 7]
        self.board = self.reset_board()

        self.winner = None
        self.ended = False

        self.num_states = 8 * 6 * 4
        self.board2state = {}
        self.compute_states()

    def compute_states(self, level = 0):
        state = 0
        for level2 in range(8):
            for level1 in range(6):
                for level0 in range(4):
                    self.board2state[int("{}{}{}".format(level2, level1, level0))] = state
                    state += 1

    def reset_board(self):
        self.board = [3, 5, 7]

    def reset(self):
        self.reset_board()
        self.winner = None
        self.ended = False

    def is_empty(self, level):
        return self.board[level] == 0

    def correct_move(self, move):
        # move -> tuple (level, number)
        level, number = move
        if level < 0 or level > 2:
            return False

        if number < 1 or number > 7:
            return False

        if (
                (level == 0 and number > self.length[0]) or
                (level == 1 and number > self.length[1]) or
                (level == 2 and number > self.length[2])
           ):
            return False

        if (
                (level == 0 and self.is_empty(level)) or
                (level == 1 and self.is_empty(level)) or
                (level == 2 and self.is_empty(level))
        ):
            return False

        if ( number > self.board[level]): return False

        return True

    def make_move(self, move):
        # move -> tuple (level, number to take)
        level, number = move
        self.board[level] -= number

    def possible_moves(self):
        # move -> tuple (level, index, number to take)
        moves = []

        for level in range(self.levels):
            for number in range(1, self.length[level] + 1):
                    movement = (level, number)
                    if self.correct_move(movement): moves.append(movement)

        return moves

    def unmake_move(self, move):
        # move -> tuple (level, number to take)
        level, number = move
        self.board[level] += number

    def reward(self, player_num):
        # win          --> V(s) = 1
        # loose        --> V(s) = 0
        if not self.game_over():
            return 0
        return 1 if self.winner == player_num else 0

    def get_state(self):
        # returns the current state
        # current state is represented as an int from 0...|S|-1, where S = set of all possible states.
        return self.board2state[int("{}{}{}".format(self.board[2], self.board[1], self.board[0]))]

    def game_over(self, force_recalculate=False):

        # shortcut
        if not force_recalculate and self.ended:
            return self.ended

        if sum(self.board) > 1:
            # game is not over
            self.winner = None
            return False

        # Game Over -> current player is the looser
        #self.winner = self.current.player
        self.ended = True
        return True

    def is_draw(self):
        return self.ended and self.winner is None

    def draw_board(self):
        for level in reversed ( range(self.levels) ):
            print("-------------")
            print("[ {} ]".format(self.board[level]))
        print("-------------")

    def play_game(self, p1, p2, draw=False):
        self.reset()
        self.current = None

        while not self.game_over():

            if self.current == p1:
                self.current = p2
            else:
                self.current = p1

            if draw:
                if draw == 1 and self.current == p1:
                    self.draw_board()
                if draw == 2 and self.current == p2:
                    self.draw_board()

            self.current.take_action(self)

            state = self.get_state()
            self.current.update_state_history(state)

        if draw:
            self.draw_board()

        p1.update(self.reward(p1.player))
        p2.update(self.reward(p2.player))

    def game_end(self):
        return sum(self.board) == 0

    def initial_values(self):
        # win          --> V(s) = 1
        # lose         --> V(s) = 0
        V = np.zeros(self.num_states)

        V[self.board2state[int("100")]] = 1
        V[self.board2state[int("010")]] = 1
        V[self.board2state[int("001")]] = 1
        return V
