from colorama import Fore, Back, Style 
from time import time

class PowerUP():
    def __init__(self, x, y, create_time, velocity_x, velocity_y):
        self.name=""
        self.create_time=create_time
        self.expire_time = 10

        if velocity_x == 0:
            self.velocity_x = 0
        elif velocity_x < 0:
            self.velocity_x = -1
        else:
            self.velocity_x = 1

        if velocity_y == 0:
            self.velocity_y = 0
        elif velocity_y < 0:
            self.velocity_y = -1
        else:
            self.velocity_y = 1

        self.x = x
        self.y = y

        self.height = 1
        self.width = 3

        self.pixel =  Back.RED+' '+Style.RESET_ALL
        self.avoid_pixel = [Back.RED+Fore.WHITE+str(i)+Style.RESET_ALL for i in range(1,9)]
        self.avoid_pixel += [self.pixel, Back.BLUE+Fore.RED+'*'+Style.RESET_ALL]
    
    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_velocity(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def get_coordinates(self, direction):
        coordinates = []
        if(direction == "left"):
            x_coord = self.x
            for row in range(self.y, self.y+self.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "right"):
            x_coord = self.x+self.width-1
            for row in range(self.y, self.y+self.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "top"):
            y_coord = self.y
            for col in range(self.x, self.x+self.width):
                coordinates.append({"x": col, "y": y_coord})
        elif(direction == "bottom"):
            y_coord = self.y+self.height-1
            for col in range(self.x, self.x+self.width):
                coordinates.append({"x": col, "y": y_coord})
        return coordinates
    
    def destroy_powerup(self, powerup, powerup_list):
        powerup_list.remove(powerup)

    def move2(self, board):
        self.y += self.velocity_y

        bottom_coordinates = self.get_coordinates("bottom")
        for coord in bottom_coordinates:
            if coord['y'] >= board.rows:
                self.destroy_powerup(self, board.generated_powerups)
                return True
            elif coord['y'] < board.rows and coord['x']>=0 and coord['x']<board.cols:
                if(board.board[coord['y']][coord['x']] != board.bg_pixel and board.board[coord['y']][coord['x']] not in self.avoid_pixel):
                    # paddle detected
                    if(coord['y'] == board.paddle.y):
                        self.destroy_powerup(self, board.generated_powerups)
                        self.create_time = time()
                        board.active_powerups.append(self)
                        return True
        return False
        

    def move(self, board):
        self.x += self.velocity_x
        self.y += self.velocity_y

        top_coordinates = self.get_coordinates("top")
        for coord in top_coordinates:
            if coord['y'] < 0:
                self.y -= self.velocity_y
                self.velocity_y = 1
                break

            
        left_coordinates = self.get_coordinates("left")
        for coord in top_coordinates:
            if coord['x'] < 0:
                self.x -= self.velocity_x
                self.velocity_x = 1
                break
        
        right_coordinates = self.get_coordinates("right")
        for coord in top_coordinates:
            if coord['x'] >= board.cols:
                self.x -= self.velocity_x
                self.velocity_x = -1
                break

        bottom_coordinates = self.get_coordinates("bottom")
        for coord in bottom_coordinates:
            if coord['y'] >= board.rows:
                self.destroy_powerup(self, board.generated_powerups)
                break
            elif coord['y'] < board.rows and coord['x']>=0 and coord['x']<board.cols:
                if(board.board[coord['y']][coord['x']] != board.bg_pixel and board.board[coord['y']][coord['x']] not in self.avoid_pixel):
                    # paddle detected
                    if(coord['y'] == board.paddle.y):
                        self.destroy_powerup(self, board.generated_powerups)
                        self.create_time = time()
                        board.active_powerups.append(self)
                        break

        if self.velocity_y == -1:
            self.velocity_y = 0
        elif self.velocity_y == 0:
            self.velocity_y = 1


class Expand_Paddle(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="1"
        self.expand_size=6

class Shrink_Paddle(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="2"
        self.shrink_size=6

class Ball_Multiplier(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="3"
        self.multiply_count=2
        self.used = False

class Fast_Ball(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="4"
        self.fast_factor_x=2
        self.fast_factor_y=2
        self.expire_time = 5

class Thru_Ball(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="5"
        self.expire_time = 5

class Paddle_Grab(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="6"

class Shooting_Paddle(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="7"
        self.expire_time = 5

class Fireball(PowerUP):
    def __init__(self, x, y, create_time, velocity_x=0, velocity_y=1):
        super().__init__(x, y, create_time, velocity_x, velocity_y)
        self.name="8"