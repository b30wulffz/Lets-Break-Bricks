from getinput import get_input
from colorama import Fore, Back, Style 
import random

class Paddle():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.height = 1
        self.width = 30

        self.pixel = Back.GREEN+' '+Style.RESET_ALL

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_dimension(self, height=1, width=10):
        self.height = height
        self.width = width

    def move(self, board):
        char = get_input()
        if(char == 'd'):
            if((self.x+self.width-1) < (board.cols-2)):
                self.x = self.x+2
                # check whether ball is touching the paddle
                if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in board.ball.get_coordinates("bottom"))):
                    # for moving ball when kept on paddle
                    if(board.ball.velocity_x == 0 and board.ball.velocity_y == 0):
                        board.ball.update_position(board.ball.x+2, board.ball.y)
            elif((self.x+self.width-1) < (board.cols-1)):
                self.x = self.x+1
                # check whether ball is touching the paddle
                if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in board.ball.get_coordinates("bottom"))):
                    # for moving ball when kept on paddle
                    if(board.ball.velocity_x == 0 and board.ball.velocity_y == 0):
                        board.ball.update_position(board.ball.x+1, board.ball.y)
        elif(char == 'a'):
            if(self.x > 1):
                self.x = self.x-2
                # check whether ball is touching the paddle
                if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in board.ball.get_coordinates("bottom"))):
                    # for moving ball when kept on paddle
                    if(board.ball.velocity_x == 0 and board.ball.velocity_y == 0):
                        board.ball.update_position(board.ball.x-2, board.ball.y)
            elif (self.x > 0):
                self.x = self.x-1
                # check whether ball is touching the paddle
                if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in board.ball.get_coordinates("bottom"))):
                    # for moving ball when kept on paddle
                    if(board.ball.velocity_x == 0 and board.ball.velocity_y == 0):
                        board.ball.update_position(board.ball.x-1, board.ball.y)
        # to launch the ball
        elif(char == 'w'):
            # check whether ball is touching the paddle
            if(any((point["x"]>=self.x and point["x"]<=(self.x+self.width-1) and point["y"]+1==self.y) for point in board.ball.get_coordinates("bottom"))):
                # for moving ball when kept on paddle
                if(board.ball.velocity_x == 0 and board.ball.velocity_y == 0):
                    board.ball.update_velocity(random.choice([-1,1]), -1)
    
        return char