import sys

class Human:
    def __init__(self):
        pass

    def set_player1(self):
        self.player = 1

    def set_player2(self):
        self.player = 2

    def take_action(self, env):
        while True:
            move = ""
            if sys.version_info[0] > 3:
                move = input("\nEnter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): ")
            else:
                move = raw_input("\nEnter level [0, 1, 2] and number of pieces to take from board separated by space (e.g. 0 3): ")

            level, number = move.split(' ')
            move = (int(level), int(number))

            if env.correct_move(move):
                env.make_move(move)
                break

    def update(self, env):
        pass

    def update_state_history(self, s):
        pass
