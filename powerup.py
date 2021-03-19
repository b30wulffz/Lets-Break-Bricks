from colorama import Fore, Back, Style 
from time import time

class PowerUP():
    def __init__(self, x, y, create_time):
        self.name=""
        self.create_time=create_time
        self.expire_time = 10

        self.velocity_y = 1

        self.x = x
        self.y = y

        self.height = 1
        self.width = 3

        self.pixel =  Back.RED+' '+Style.RESET_ALL
        self.avoid_pixel = [Back.RED+Fore.WHITE+str(i)+Style.RESET_ALL for i in range(1,8)]
        self.avoid_pixel.append(self.pixel)

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

    def move(self, board):
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

class Expand_Paddle(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="1"
        self.expand_size=6

class Shrink_Paddle(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="2"
        self.shrink_size=6

class Ball_Multiplier(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="3"
        self.multiply_count=2
        self.used = False

class Fast_Ball(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="4"
        self.fast_factor_x=2
        self.fast_factor_y=2
        self.expire_time = 5

class Thru_Ball(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="5"
        self.expire_time = 5

class Paddle_Grab(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="6"

class Shooting_Paddle(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="7"
        self.expire_time = 5