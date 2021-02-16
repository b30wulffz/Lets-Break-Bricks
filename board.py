from os import system
from paddle import Paddle
from ball import Ball

class Board():

    def __init__(self, bricks=[], balls=[]):
        self.cols = 80
        self.rows = 32
        self.paddle = Paddle(self.cols//2 -6 , self.rows-1) # moving paddle to center
        self.ball = Ball(self.cols//2 - 2, self.rows-2) # moving ball on top of paddle
        self.render()

    def render(self):

        system('clear')
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]
        # self.board = []
        # for j in range(self.rows+2):
        #     row = []
        #     for i in range(self.cols+2):
        #         if(i==0 or i==self.cols+1):
        #             row.append('|')
        #         else:
        #             row.append('.')
        #     self.board.append(row)

        # render paddle
        for row in range(self.paddle.y, self.paddle.y+self.paddle.height):
            for col in range(self.paddle.x, self.paddle.x+self.paddle.width):
                self.board[row][col] = self.paddle.pixel

        # render ball

        # updating distance based on velocity
        self.ball.update_position(self.ball.x+self.ball.velocity_x, self.ball.y+self.ball.velocity_y)

        # checking for collisions
        
        # left wall collision

        # right wall collision

        # top wall collision

        # bottom wall collision

        # paddle collision

        # brick collision

        # if collision update its position to collision location and update velocity

        for row in range(self.ball.y, self.ball.y+self.ball.height):
            for col in range(self.ball.x, self.ball.x+self.ball.width):
                self.board[row][col] = self.ball.pixel

        # adding borders to board
        height = 4
        width= self.cols
        wall = 1
        self.output = [['#' for i in range(width+2*wall)] for j in range(height+2*wall)]
        self.output.extend([['#' for i in range(self.cols+2*wall)] for j in range(self.rows+2*wall)])
        for j in range(wall, self.rows+wall):
            for i in range(wall, self.cols+wall):
                self.output[j+height+wall+1][i] = self.board[j-wall][i-wall]

        print("\n".join(["".join(row) for row in self.output]))
