from getinput import get_input
from colorama import Fore, Back, Style 
import random

class Paddle():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.initial_width = 30

        self.height = 1
        self.width = 30

        self.pixel = Back.GREEN+' '+Style.RESET_ALL
        self.bullets = []
        self.bullet_launcher_pixel = Back.MAGENTA+' '+Style.RESET_ALL

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_dimension(self, height=1, width=30):
        self.height = height
        self.width = width

    def move(self, board):
        char = get_input()
        if(char == 'd'):
            if((self.x+self.width-1) < (board.cols-2)):
                # check whether ball is touching the paddle
                move = True
                for ball in board.balls:
                    if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in ball.get_coordinates("bottom"))):
                        # for moving ball when kept on paddle
                        if(ball.velocity_x == 0 and ball.velocity_y == 0 or ball.hold):
                            if(ball.x+ball.width-1 < (board.cols-2)):
                                ball.update_position(ball.x+2, ball.y)
                            else:
                                move = False
                if(move):
                    self.x = self.x+2
                    if board.boss is not None:
                        board.boss.x += 2
            elif((self.x+self.width-1) < (board.cols-1)):
                # check whether ball is touching the paddle
                move = True
                for ball in board.balls:
                    if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in ball.get_coordinates("bottom"))):
                        # for moving ball when kept on paddle
                        if(ball.velocity_x == 0 and ball.velocity_y == 0 or ball.hold):
                            if(ball.x+ball.width-1 < (board.cols-1)):
                                ball.update_position(ball.x+1, ball.y)
                            else:
                                move = False
                if(move):
                    self.x = self.x+1
                    if board.boss is not None:
                        board.boss.x += 1
        elif(char == 'a'):
            if(self.x > 1):
                # check whether ball is touching the paddle
                move = True
                for ball in board.balls:
                    if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in ball.get_coordinates("bottom"))):
                        # for moving ball when kept on paddle
                        if(ball.velocity_x == 0 and ball.velocity_y == 0 or ball.hold):
                            if(ball.x > 1):
                                ball.update_position(ball.x-2, ball.y)
                            else:
                                move = False
                if(move):
                    self.x = self.x-2
                    if board.boss is not None:
                        board.boss.x -= 2
            elif (self.x > 0):
                # check whether ball is touching the paddle
                move = True
                for ball in board.balls:
                    if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in ball.get_coordinates("bottom"))):
                        # for moving ball when kept on paddle
                        if(ball.velocity_x == 0 and ball.velocity_y == 0 or ball.hold):
                            if(ball.x > 0):
                                ball.update_position(ball.x-1, ball.y)
                            else:
                                move = False
                if(move):
                    self.x = self.x-1
                    if board.boss is not None:
                        board.boss.x -= 1
        # to launch the ball
        elif(char == 'w'):
            # check whether ball is touching the paddle
            for ball in board.balls:
                if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in ball.get_coordinates("bottom"))):
                    # for moving ball when kept on paddle
                    if(ball.velocity_x == 0 and ball.velocity_y == 0):
                        ball.update_velocity(random.choice([-1,1]), -1)
                    if(ball.hold):
                        ball.hold = False  

        # debug for level up
        elif(char == 'p'):
            board.bricks = []           
        
        return char