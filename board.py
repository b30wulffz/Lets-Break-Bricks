from colorama import Fore, Back, Style 
from os import system
from paddle import Paddle
from ball import Ball

class Board():

    def __init__(self, bricks=[], balls=[]):
        self.cols = 80
        self.rows = 34
        self.paddle = Paddle(self.cols//2 -6 , self.rows-1) # moving paddle to center
        self.ball = Ball(self.cols//2 - 2, self.rows-2) # moving ball on top of paddle
        self.score = 0
        self.lives = 3
        self.render()

    def render(self):

        system('clear')
        bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.board = [[bg_pixel for i in range(self.cols)] for j in range(self.rows)]
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
        score_board_height = 4
        wall = 1
        border_pixel = Back.BLUE+' '+Style.RESET_ALL

        self.output = [[border_pixel for i in range(self.cols+2*wall)] for j in range(score_board_height+self.rows+2*wall)]
        # self.output.extend([[border_pixel for i in range(self.cols+2*wall)] for j in range(self.rows+2*wall)])

        title = "Lets Break Bricks"
        title_offset = (self.cols+wall-len(title)) // 2
        for j in range(0, len(title)):
            self.output[1][title_offset+j] = Back.BLUE+Fore.MAGENTA+title[j]+Style.RESET_ALL
        
        score_text = "Score: {}".format(self.score)
        score_text_offset = (self.cols+wall-len(score_text)) // 8
        for j in range(0, len(score_text)):
            self.output[3][score_text_offset+j] = Back.BLUE+Fore.MAGENTA+score_text[j]+Style.RESET_ALL
        
        lives_text = "Lives: {}".format(self.lives)
        lives_text_offset = (self.cols+wall-len(lives_text)) * 7 // 8
        for j in range(0, len(lives_text)):
            self.output[3][lives_text_offset+j] = Back.BLUE+Fore.MAGENTA+lives_text[j]+Style.RESET_ALL
        
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+score_board_height+wall][i+wall] = self.board[j][i]

        print("\n".join(["".join(row) for row in self.output]))
