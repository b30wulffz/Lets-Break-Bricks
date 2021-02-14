from os import system
from paddle import Paddle
from colorama import Fore, Back, Style 

class Board():

    def __init__(self, bricks=[], balls=[]):
        self.cols = 80
        self.rows = 40
        self.paddle = Paddle(self.cols//2 -6 , self.rows-1) # moving paddle to center
        self.render()

    def render(self):

        system('clear')
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]

        # render paddle
        for row in range(self.paddle.y,  self.paddle.y+self.paddle.height):
            for col in range(self.paddle.x, self.paddle.x+self.paddle.width):
                self.board[row][col] = Back.GREEN+' '+Style.RESET_ALL
        
        print("\n".join(["".join(row) for row in self.board]))
