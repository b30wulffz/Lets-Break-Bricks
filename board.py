from os import system
from paddle import Paddle
from ball import Ball

class Board():

    def __init__(self, bricks=[], balls=[]):
        self.cols = 80
        self.rows = 35
        self.paddle = Paddle(self.cols//2 -6 , self.rows-1) # moving paddle to center
        self.ball = Ball(self.cols//2 - 2, self.rows-2) # moving ball on top of paddle
        self.render()

    def render(self):

        system('clear')
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]

        # render paddle
        for row in range(self.paddle.y, self.paddle.y+self.paddle.height):
            for col in range(self.paddle.x, self.paddle.x+self.paddle.width):
                self.board[row][col] = self.paddle.pixel

        # render ball

        # updating distance based on velocity
        self.ball.update_position(self.ball.x+self.ball.velocity_x, self.ball.y+self.ball.velocity_y)

        # checking for collisions
        
        # left wall collision

        for row in range(self.ball.y, self.ball.y+self.ball.height):
            for col in range(self.ball.x, self.ball.x+self.ball.width):
                self.board[row][col] = self.ball.pixel

        print("\n".join(["".join(row) for row in self.board]))
