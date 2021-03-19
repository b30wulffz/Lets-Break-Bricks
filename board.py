from colorama import Fore, Back, Style 
from os import system
from paddle import Paddle
from ball import Ball
from brick import EasyBrick, MediumBrick, HardBrick, UnbreakableBrick, SuperBrick
from powerup import Expand_Paddle, Shrink_Paddle, Ball_Multiplier, Fast_Ball, Thru_Ball, Paddle_Grab, Shooting_Paddle, Fireball
from pattern import Pattern
from bullet import Bullet
from boss import Boss
import random
from time import sleep,time
import math

class Board():

    def __init__(self, balls=[]):
        self.cols = 84
        self.rows = 31
        self.paddle = Paddle(self.cols//2 -12 , self.rows-1) # moving paddle to center
        self.balls = [Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.initial_width-2), self.rows-2)] # moving ball on top of paddle at a random position
        self.score = 0
        self.lives = 3
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.startTime = time()
        self.currentTime = time()
        self.generated_powerups = []
        self.active_powerups = []
        self.game_over = False
        self.level = 1
        self.ticks = 0
        self.boss = None

        # generate bricks
        ub = UnbreakableBrick(0,0)
        x, y = 1, 1

        self.bricks = Pattern.level_1(self.cols)
        self.render()


    def initialise(self):
        self.paddle.update_dimension(self.paddle.height, self.paddle.initial_width)
        if(self.paddle.x+self.paddle.initial_width-1 >=self.cols):
            self.paddle.x -= self.paddle.x + self.paddle.initial_width - self.cols
        self.balls = [Ball(random.randrange(self.paddle.x, self.paddle.x+self.paddle.initial_width-2), self.rows-2)]
        self.generated_powerups = []
        self.active_powerups = []
        self.paddle.bullets = []


    def spawn_powerups(self, brick, velocities):
        probability = random.randint(1,101)
        
        if(probability<40):
            temp_powerup = Expand_Paddle(0,0,0,0,1)
            powerup_choice = random.choice([1,2,3,4,5,6,7,8])
            if velocities is not None:
                vel_x = velocities[0]
                vel_y = velocities[1]
            else:
                vel_x = 0
                vel_y = 1
            x = random.randint(brick.x, brick.x+brick.width-temp_powerup.width)
            if(powerup_choice == 1):
                self.generated_powerups.append(Expand_Paddle(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 2):
                self.generated_powerups.append(Shrink_Paddle(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 3):
                self.generated_powerups.append(Ball_Multiplier(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 4):
                self.generated_powerups.append(Fast_Ball(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 5):
                self.generated_powerups.append(Thru_Ball(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 6):
                self.generated_powerups.append(Paddle_Grab(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 7):
                self.generated_powerups.append(Shooting_Paddle(x, brick.y, time(), vel_x, vel_y))
            elif(powerup_choice == 8):
                self.generated_powerups.append(Fireball(x, brick.y, time(), vel_x, vel_y))
                
    def brick_detect_and_remove(self, x, y, forced=False, fireball_trigger=False, velocities=None):
        score = 0
        fireball_powerup = None
        for powerup in self.active_powerups:
            if(type(powerup) is Fireball):
                fireball_powerup = powerup
                break
        for brick in self.bricks:
            x_lower = brick.x
            x_upper = brick.x + brick.width -1
            y_lower = brick.y
            y_upper = brick.y + brick.height -1
            if( x_lower <= x and x_upper >= x and y_lower <= y and y_upper >= y):
                if(type(brick) is SuperBrick or (fireball_powerup is not None and fireball_trigger == False)):
                    score = brick.reduce_health(True)
                    self.score += score
                    self.bricks.remove(brick)
                    if brick.is_bosslayer == False:
                        self.spawn_powerups(brick, velocities)
                    for y in range(brick.y-2, brick.y+brick.height-1+3):
                        for x in range(brick.x-4, brick.x+brick.width-1+4):
                            self.brick_detect_and_remove(x,y,True,True)
                else:    
                    score = brick.reduce_health(forced)
                    if score > 0:
                        self.score += score
                        self.bricks.remove(brick)
                        if brick.is_bosslayer == False:
                            self.spawn_powerups(brick, velocities)
                return True
        # check for boss
        if self.boss is not None:
            x_lower = self.boss.x
            x_upper = self.boss.x + self.boss.width - 1
            y_lower = self.boss.y
            y_upper = self.boss.y + self.boss.height - 1
            if( x_lower <= x and x_upper >= x and y_lower <= y and y_upper >= y):
                self.boss.reduce_health()
                return False

        return False

    def no_bricks_left(self):
        if(not any((type(brick) is not UnbreakableBrick) for brick in self.bricks)): 
            if self.level < 3:
                if self.level == 1:
                    self.bricks = Pattern.level_2(self.cols)
                elif self.level == 2:
                    self.bricks = Pattern.level_3(self.cols)
                    self.boss = Boss(self.paddle.x+6, 0)
                self.level+=1
                self.initialise()
            else:
                if self.boss is not None:
                    if self.boss.health == 0:
                        self.game_over = True

    def shift_bricks(self):
        cutoff = 600
        if self.level == 2:
            cutoff = 400
        elif self.level == 3:
            cutoff = 500
        if self.ticks > cutoff:
            for brick in self.bricks:
                brick.y += 1
                # check for brick paddle collision
                if brick.y >= self.paddle.y-1:
                    self.game_over = True
            self.ticks = 0
    
    def render(self):
        system('clear')
        self.board = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]

        # render paddle
        for row in range(self.paddle.y, self.paddle.y+self.paddle.height):
            for col in range(self.paddle.x, self.paddle.x+self.paddle.width):
                self.board[row][col] = self.paddle.pixel

        # render bricks
        for brick in self.bricks:
            if (self.ticks % 4) == 0:
                brick.trigger_rainbow()
            for row in range(brick.y, brick.y+brick.height):
                for col in range(brick.x, brick.x+brick.width):
                    self.board[row][col] = brick.pixel

        # render boss and bombs
        if self.boss is not None:
            self.boss.render(self)

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
                if(type(powerup) is Ball_Multiplier):
                    # remove nearest ball from floor
                    if(len(self.balls)>1):
                        nearest_ball = self.balls[0]
                        for ball in self.balls:
                            if(nearest_ball.y < ball.y):
                                nearest_ball=ball
                        self.balls.remove(nearest_ball)
                    
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

        # activate ball multiplier
        for powerup in self.active_powerups:
            if(type(powerup) is Ball_Multiplier and powerup.used == False):                
                # multiply farthest ball from floor
                if(len(self.balls)>0):
                    reference_ball = self.balls[0]
                    for ball in self.balls:
                        if(reference_ball.y > ball.y):
                            reference_ball=ball
                    new_ball = Ball(reference_ball.x, reference_ball.y)
                    new_ball.velocity_y = reference_ball.velocity_y
                    if(reference_ball.velocity_x == 0):
                        new_ball.velocity_x = random.choice([-1,1])
                    else:
                        new_ball.velocity_x = -reference_ball.velocity_x
                    self.balls.append(new_ball)
                powerup.used = True

        # activate shooting paddle powerup
        shooting_paddle_powerup = None
        for powerup in self.active_powerups:
            if(type(powerup) is Shooting_Paddle):
                shooting_paddle_powerup = powerup
                break

        if shooting_paddle_powerup is not None:

            # paddle cannon points
            for row in range(self.paddle.y, self.paddle.y+self.paddle.height):
                for col in [self.paddle.x, self.paddle.x+self.paddle.width-1]:
                    self.board[row][col] = self.paddle.bullet_launcher_pixel

            # generate bullets
            if(self.ticks % 7 == 0):
                tmp_bullet = Bullet(0,0)
                self.paddle.bullets.append(Bullet(self.paddle.x, self.paddle.y-tmp_bullet.height))
                self.paddle.bullets.append(Bullet(self.paddle.x+self.paddle.width-tmp_bullet.width, self.paddle.y-tmp_bullet.height))
            
        # render bullets
        for bullet in self.paddle.bullets:
            bullet.move(self)
            for row in range(bullet.y, bullet.y+bullet.height):
                for col in range(bullet.x, bullet.x+bullet.width):
                    self.board[row][col] = bullet.pixel

        # render ball
        if(len(self.balls) == 0):
            if(self.lives > 0):
                self.initialise()
                self.lives-=1

        if(self.lives > 0 and self.game_over == False):
            for ball in self.balls:
                ball.move(self) # checking ball collision here itself
                if ball in self.balls:
                    for row in range(ball.y, ball.y+ball.height):
                        for col in range(ball.x, ball.x+ball.width):
                            # print("->", (col, row))
                            self.board[row][col] = ball.pixel
        else: 
            self.game_over = True

        # check for the case when no bricks are left
        self.no_bricks_left()

        # adding borders to board
        score_board_height = 8
        wall = 1
        border_pixel = Back.BLUE+' '+Style.RESET_ALL

        self.output = [[border_pixel for i in range(self.cols+2*wall)] for j in range(score_board_height+self.rows+2*wall)]

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
        time_taken_offset = (self.cols+wall-len(time_taken)) * 3 //8
        for j in range(0, len(time_taken)):
            self.output[3][time_taken_offset+j] = Back.BLUE+Fore.RED+time_taken[j]+Style.RESET_ALL
        
        text = "Level: {}".format(self.level)
        offset = (self.cols+wall-len(text)) * 5 // 8
        for j in range(0, len(text)):
            self.output[3][offset+j] = Back.BLUE+Fore.RED+text[j]+Style.RESET_ALL

        lives_text = "Lives: {}".format(self.lives)
        lives_text_offset = (self.cols+wall-len(lives_text)) * 7 // 8
        for j in range(0, len(lives_text)):
            self.output[3][lives_text_offset+j] = Back.BLUE+Fore.RED+lives_text[j]+Style.RESET_ALL
        
        if self.boss is not None:
            health_bar_len = 40
            text = "Boss: "
            offset = (self.cols+wall-len(lives_text)-health_bar_len) // 2
            for j in range(0, len(text)):
                self.output[7][offset+j] = Back.BLUE+Fore.RED+text[j]+Style.RESET_ALL
            for j in range(0, health_bar_len):
                self.output[7][len(text)+offset+j] = Back.BLACK+" "+Style.RESET_ALL
            boss_health = int(self.boss.health * health_bar_len / self.boss.max_health)
            for j in range(0, boss_health):
                self.output[7][len(text)+offset+j] = Back.YELLOW+" "+Style.RESET_ALL
            
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
            self.ticks += 1