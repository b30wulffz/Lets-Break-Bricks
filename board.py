from colorama import Fore, Back, Style 
from os import system
from paddle import Paddle
from ball import Ball
from brick import EasyBrick, MediumBrick, HardBrick, UnbreakableBrick, SuperBrick
from powerup import Expand_Paddle, Shrink_Paddle, Ball_Multiplier, Fast_Ball, Thru_Ball, Paddle_Grab
import random
from time import sleep,time
import math

class Board():

    def __init__(self, balls=[]):
        self.cols = 84
        # self.rows = 30
        self.rows = 34
        self.paddle = Paddle(self.cols//2 -12 , self.rows-1) # moving paddle to center
        # self.ball = Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.width-2), self.rows-2) # moving ball on top of paddle at a random position
        self.balls = [Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.initial_width-2), self.rows-2)]# moving ball on top of paddle at a random position
        self.score = 0
        self.lives = 3
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.startTime = time()
        self.currentTime = time()
        self.generated_powerups = []
        self.active_powerups = []
        self.game_over = False

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


    def initialise(self):
        self.paddle.update_dimension(self.paddle.height, self.paddle.initial_width)
        if(self.paddle.x+self.paddle.initial_width-1 >=self.cols):
            self.paddle.x -= self.paddle.x + self.paddle.initial_width - self.cols
        self.balls = [Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.initial_width-2), self.rows-2)]
        self.generated_powerups = []
        self.active_powerups = []


    def spawn_powerups(self, brick):
        # probability = random.randint(1,101)
        probability = 15
        
        if(probability<20):
            # powerup_choice = random.choice([1,2,3,4,5,6])
            temp_powerup = Expand_Paddle(0,0,0)
            powerup_choice = random.choice([1,2])
            if(powerup_choice == 1):
                x = random.randint(brick.x, brick.x+brick.width-temp_powerup.width)
                self.generated_powerups.append(Expand_Paddle(x, brick.y, time()))
            elif(powerup_choice == 2):
                x = random.randint(brick.x, brick.x+brick.width-temp_powerup.width)
                self.generated_powerups.append(Shrink_Paddle(x, brick.y, time()))
            elif(powerup_choice == 4):
                x = random.randint(brick.x, brick.x+brick.width-temp_powerup.width)
                self.generated_powerups.append(Fast_Ball(x, brick.y, time()))
                
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
                    self.spawn_powerups(brick)
                    for y in range(brick.y-2, brick.y+brick.height-1+3):
                        for x in range(brick.x-4, brick.x+brick.width-1+4):
                            self.brick_detect_and_remove(x,y,True)
                else:    
                    score = brick.reduce_health(forced)
                    if score > 0:
                        self.score += score
                        self.bricks.remove(brick)
                        self.spawn_powerups(brick)
                return True
        return False

    def render(self):
        system('clear')
        self.board = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]
        # print(len(self.board[0]))
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

        # render powerup
        for powerup in self.generated_powerups:
            text = powerup.name
            text_offset =powerup.x+ (powerup.width-len(text)) // 2
            for row in range(powerup.y, powerup.y+powerup.height):
                for col in range(powerup.x, powerup.x+powerup.width):
                    self.board[row][col] = powerup.pixel
            for j in range(0, len(text)):
                self.board[powerup.y][text_offset+j] = Back.RED+Fore.WHITE+text[j]+Style.RESET_ALL
            
            powerup.move(self)

        # deactivate powerup after a fixed time interval
        for powerup in self.active_powerups:
            if(math.floor(self.currentTime-powerup.create_time) >= powerup.expire_time):
                powerup.destroy_powerup(powerup, self.active_powerups)

        # activate expand paddle
        expand_paddle_powerup = None
        for powerup in self.active_powerups:
            if(type(powerup) is Expand_Paddle):
                expand_paddle_powerup = powerup
                break
            
        # activate shrink paddle
        shrink_paddle_powerup = None
        for powerup in self.active_powerups:
            if(type(powerup) is Shrink_Paddle):
                shrink_paddle_powerup = powerup
                break
        
        paddle_init_width = self.paddle.initial_width
        if(expand_paddle_powerup is not None):
            paddle_init_width += expand_paddle_powerup.expand_size 
        if(shrink_paddle_powerup is not None):
            paddle_init_width -= shrink_paddle_powerup.shrink_size 
        
        self.paddle.update_dimension(self.paddle.height, paddle_init_width)
        if(self.paddle.x+paddle_init_width >= self.cols):
            self.paddle.x -= self.paddle.x + paddle_init_width - self.cols

        # render ball

        # updating distance based on velocity
        # self.ball.update_position(self.ball.x+self.ball.velocity_x, self.ball.y+self.ball.velocity_y)

        # checking for collisions
        
        # left wall collision

        # right wall collision

        # top wall collision

        # bottom wall collision

        # paddle collision

        # brick collision

        # if collision update its position to collision location and update velocity

        if(len(self.balls) == 0):
            if(self.lives > 0):
                self.initialise()
                self.lives-=1

        if(self.lives > 0 and self.game_over == False):
            for ball in self.balls:
                ball.move(self)
                if ball in self.balls:
                    for row in range(ball.y, ball.y+ball.height):
                        for col in range(ball.x, ball.x+ball.width):
                            # print("->", (col, row))
                            self.board[row][col] = ball.pixel
        else: 
            self.game_over = True

        if(not any((type(brick) is not UnbreakableBrick) for brick in self.bricks)): 
            self.game_over = True


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
        
        time_elpsed = math.floor(self.currentTime-self.startTime)
        time_taken = "Time: {} seconds".format(time_elpsed)
        time_taken_offset = (self.cols+wall-len(time_taken)) * 4 //8
        for j in range(0, len(time_taken)):
            self.output[3][time_taken_offset+j] = Back.BLUE+Fore.RED+time_taken[j]+Style.RESET_ALL

        lives_text = "Lives: {}".format(self.lives)
        lives_text_offset = (self.cols+wall-len(lives_text)) * 7 // 8
        for j in range(0, len(lives_text)):
            self.output[3][lives_text_offset+j] = Back.BLUE+Fore.RED+lives_text[j]+Style.RESET_ALL
        
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+score_board_height+wall][i+wall] = self.board[j][i]

        
        if self.game_over == True:
            game_over_screen_height = 7
            game_over_screen_width = self.cols//2
            self.game_over_screen = [[border_pixel for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]

            game_over = "Game Over!"
            game_over_offset = (game_over_screen_width-len(game_over)) // 2
            for j in range(0, len(game_over)):
                self.game_over_screen[1][game_over_offset+j] = Back.BLUE+Fore.RED+game_over[j]+Style.RESET_ALL

            score_text = "Score: {}".format(self.score)
            score_text_offset = (game_over_screen_width-len(score_text)) // 2
            for j in range(0, len(score_text)):
                self.game_over_screen[3][score_text_offset+j] = Back.BLUE+Fore.RED+score_text[j]+Style.RESET_ALL

            time_taken = "Time Taken: {} seconds".format(time_elpsed)
            time_taken_offset = (game_over_screen_width-len(time_taken)) // 2
            for j in range(0, len(time_taken)):
                self.game_over_screen[5][time_taken_offset+j] = Back.BLUE+Fore.RED+time_taken[j]+Style.RESET_ALL

            height_offset = score_board_height+((self.rows//2)-(game_over_screen_height//2)+1)
            width_offset = 2*wall+((self.cols//2)-(game_over_screen_width//2)) 
            for row in range(0, game_over_screen_height):
                for col in range(0, game_over_screen_width):
                    self.output[height_offset+row][width_offset+col] = self.game_over_screen[row][col]

        print("\n".join(["".join(row) for row in self.output]))

        if(self.game_over ==  False):
            self.currentTime = time()