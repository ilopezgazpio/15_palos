import pygame
from Point import Point
from Stick import Stick
from Sticks import Sticks
from Scene import Scene
from Environment import Environment
from Agent import Agent
from Human_Agent import Human
import time
import os

class GameScene(Scene):

    def __init__(self, args = {}):
        '''Initialize'''
        Scene.__init__(self, args)

        ''' define local objects and sprites '''

        # Initialize environment
        self.env = Environment()

        # Game turn variables
        self.drawPlayer = None
        self.currentPlayer = None

        # Initialize AI player
        self.aiPlayer = Agent(self.args.epsilon, self.args.alpha)
        self.aiPlayer.loadAgentValues(self.args.path)
        self.aiPlayer.eps = 0
        self.aiPlayer.set_verbose(True)

        # Initialize Human player
        self.human = Human()

        # TODO Initialize rounds - Implemented in generic resetGameScene
        # self.env.reset()
        #self.initialized = False
        self.rounds = -1
        ''' Create objects of game'''
        # todo -> scene knows about args -> get args.resolution
        #self.sticks = Sticks()
        self.resetGameScene()
        # print("Starting round {}".format(rounds))

        # Read agent Vs files
        if not os.path.exists(args.path):
            print("File {0} with V(s) values of agent does not exist. First run training script".format(args.path))
            self.showing = False
            self.next_scene = 'VSFileNotFoundScene'

        ''' define background '''
        self.background_image = pygame.image.load("resources/BMP/fieltro.bmp").convert()

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_sprite = Point(pygame.mouse.get_pos())
                stick_clicked = pygame.sprite.spritecollide(mouse_sprite, self.sticks, False)
                # Debug
                # mouse_sprite.printRect()
                # for stick in stick_clicked:
                #    stick.printRect()
                if stick_clicked:
                    stick_clicked[0].clicked()

            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
                # TODO - ILLEGAL MOVEMENT CONTROL
                level, number = self.sticks.removeSelected()
                move = (int(level), int(number))
                self.env.make_move(move)

                # Debug
                print("Level: {0} , Number: {1}".format(level, number))
                print("==============")
                print("Human Movement")
                print("==============")
                self.env.draw_board()

                # Give turn
                self.currentPlayer = self.aiPlayer

    def update(self):
        '''Game iteration'''
        if len(self.sticks) == 1:
            time.sleep(2)
            print("=========")
            print("Game Over")
            print("=========")
            self.resetGameScene()
            self.next_scene = 'GameOverScene'
        else:
            self.next_scene = None

        # Set starting player for the whole round
        if not self.initialized and self.rounds % 2 == 0:
            self.aiPlayer.set_player1()
            self.human.set_player2()
            # self.env.play_game(aiPlayer, human, draw=2), for pygame we need to decompose this call
            self.initialized = True
            self.currentPlayer = self.human
            self.drawPlayer = 2

        elif not self.initialized and self.rounds %2 != 0:
            self.aiPlayer.set_player2()
            self.human.set_player1()
            # self.env.play_game(human, aiPlayer, draw=1), for pygame we need to decompose this call
            self.initialized = True
            self.currentPlayer = self.aiPlayer
            self.darwPlayer = 1

        # Game turn

        # 1 - Draw board if debug is necessary
        #self.env.draw_board()

        # 2 - if AI agent turn -> then take action
        if self.currentPlayer == self.aiPlayer:

            # ai_move is always a valid move
            ai_move = self.currentPlayer.take_action(self.env)
            self.sticks.removeMovement(ai_move)

            # 3 - Update environment state
            env_state = self.env.get_state()

            # 4 - Update state history
            self.currentPlayer.update_state_history(env_state)

            # 5 - Give turn
            self.currentPlayer = self.human

        self.sticks.update()

    def draw(self, screen):
        '''Fill screen background'''
        dimension = screen.get_size()
        self.background_image = pygame.transform.scale(self.background_image, dimension)
        screen.blit(self.background_image, [0,0])

        '''Draw sticks'''
        self.sticks.draw(screen)

    def game_over(self):
        message = ""
        return self.env.game_over()


    def resetGameScene(self):
        self.next_scene = None
        self.sticks = Sticks()
        self.env.reset()
        self.rounds += 1
        self.initialized = False

