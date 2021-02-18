from colorama import Fore, Back, Style 

class Brick():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 1
        self.width = 6

    def check_collision(self):
        pass

class EasyBrick(Brick):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 1
        self.pixel =  Back.YELLOW+' '+Style.RESET_ALL
    
class HardBrick(Brick):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 2
        self.pixel =  Back.CYAN+' '+Style.RESET_ALL
    
class UnbreakableBrick(Brick):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.health = -1
        self.pixel =  Back.MAGENTA+' '+Style.RESET_ALL
    