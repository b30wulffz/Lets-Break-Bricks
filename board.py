from colorama import Fore, Back, Style 
from os import system
from paddle import Paddle
from ball import Ball
from brick import EasyBrick, MediumBrick, HardBrick, UnbreakableBrick, SuperBrick
import random

class Board():

    def __init__(self, balls=[]):
        self.cols = 84
        # self.rows = 30
        self.rows = 34
        self.paddle = Paddle(self.cols//2 -12 , self.rows-1) # moving paddle to center
        self.ball = Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.width-2), self.rows-2) # moving ball on top of paddle at a random position
        self.score = 0
        self.lives = 3
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL

        # generate bricks
        ub = UnbreakableBrick(0,0)
        x, y = 1, 1

        self.bricks = []

        while True:
            # if (y-1)%4 == 0:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            
                # x = 
            while True:
                if((x+ub.width)>=self.cols):
                    break
                index = random.choice([0,0,0,1,1,2])
                if(index == 0):
                    self.bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    self.bricks.append(MediumBrick(x,y))
                else:
                    self.bricks.append(HardBrick(x,y))
                x+=ub.width+1
                # print((x,y), end=" ")
            y+=ub.height+1
            # print()
            if(y>=8):
                    break

        if(len(self.bricks) > 6):
            ind = random.randint(2,6)
            self.bricks[ind] = UnbreakableBrick(self.bricks[ind].x, self.bricks[ind].y)
        if(len(self.bricks) > 20):
            ind = random.randint(20,20)
            self.bricks[ind] = UnbreakableBrick(self.bricks[ind].x, self.bricks[ind].y)
        if(len(self.bricks) > 38):
            ind = random.randint(35,38)
            self.bricks[ind] = UnbreakableBrick(self.bricks[ind].x, self.bricks[ind].y)
            
        ind = random.choice([13, 14, 29])
        if(len(self.bricks) > ind):
            self.bricks[ind] = SuperBrick(self.bricks[ind].x, self.bricks[ind].y)

        self.render()

    def brick_detect_and_remove(self, x, y, forced=False):
        score = 0
        for brick in self.bricks:
            x_lower = brick.x
            x_upper = brick.x + brick.width -1
            y_lower = brick.y
            y_upper = brick.y + brick.height -1
            if( x_lower <= x and x_upper >= x and y_lower <= y and y_upper >= y):
                if(type(brick) is SuperBrick):
                    score = brick.reduce_health(True)
                    self.score += score
                    self.bricks.remove(brick)
                    for y in range(brick.y-2, brick.y+brick.height-1+3):
                        for x in range(brick.x-4, brick.x+brick.width-1+4):
                            self.brick_detect_and_remove(x,y,True)
                else:    
                    score = brick.reduce_health(forced)
                    if score > 0:
                        self.score += score
                        self.bricks.remove(brick)
                return True
        return False

    def render(self):

        system('clear')
        self.board = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]
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

        # render bricks
        for brick in self.bricks:
            for row in range(brick.y, brick.y+brick.height):
                for col in range(brick.x, brick.x+brick.width):
                    self.board[row][col] = brick.pixel

        # render ball

        # updating distance based on velocity
        # self.ball.update_position(self.ball.x+self.ball.velocity_x, self.ball.y+self.ball.velocity_y)
        self.ball.move(self)

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
                # print("->", (col, row))
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
            self.output[1][title_offset+j] = Back.BLUE+Fore.RED+title[j]+Style.RESET_ALL
        
        score_text = "Score: {}".format(self.score)
        score_text_offset = (self.cols+wall-len(score_text)) // 8
        for j in range(0, len(score_text)):
            self.output[3][score_text_offset+j] = Back.BLUE+Fore.RED+score_text[j]+Style.RESET_ALL
        
        lives_text = "Lives: {}".format(self.lives)
        lives_text_offset = (self.cols+wall-len(lives_text)) * 7 // 8
        for j in range(0, len(lives_text)):
            self.output[3][lives_text_offset+j] = Back.BLUE+Fore.RED+lives_text[j]+Style.RESET_ALL
        
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+score_board_height+wall][i+wall] = self.board[j][i]

        print("\n".join(["".join(row) for row in self.output]))
