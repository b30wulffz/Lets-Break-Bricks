from colorama import Fore, Back, Style 

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

    def destroy_powerup(self, powerup, powerup_list):
        powerup_list.remove(powerup)

class Expand_Paddle(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="1"
        self.expand_size=2

class Shrink_Paddle(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="2"
        self.shrink_size=2

class Ball_Multiplier(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="3"
        self.multiply_count=2

class Fast_Ball(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="4"
        self.fast_factor_x=2
        self.fast_factor_y=2

class Thru_Ball(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="5"

class Paddle_Grab(PowerUP):
    def __init__(self, x, y, create_time):
        super().__init__(x, y, create_time)
        self.name="6"