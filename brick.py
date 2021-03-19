from colorama import Fore, Back, Style 
from time import sleep
import random

class Brick():
    
    def __init__(self, x, y, is_bosslayer = False):
        self.x = x
        self.y = y
        self.height = 1
        self.width = 6   
        self.health = -1
        self.score = 0
        self.is_rainbow = False
        self.is_bosslayer = is_bosslayer

    def reduce_health(self, forced=False):
        if self.is_rainbow == True:
            self.is_rainbow = False
        if(forced == True):
            self.health = 0
            return self.score
        else:
            if(self.health > 0):
                self.health -= 1
                if(self.health == 2):
                    self.pixel =  Back.CYAN+' '+Style.RESET_ALL
                if(self.health == 1):
                    self.pixel =  Back.YELLOW+' '+Style.RESET_ALL
                elif(self.health == 0):
                    return self.score
        return 0

    def trigger_rainbow(self):
        if self.is_rainbow == True:
            health_values = list(filter(lambda x: x != self.health, [1,2,3]))
            health = random.choice(health_values)
            self.health = health
            if self.health == 1:
                self.pixel =  Back.YELLOW+' '+Style.RESET_ALL
                self.score = 100
            elif self.health == 2:
                self.pixel =  Back.CYAN+' '+Style.RESET_ALL
                self.score = 200
            elif self.health == 3:
                self.pixel =  Back.MAGENTA+' '+Style.RESET_ALL
                self.score = 300

class EasyBrick(Brick):

    def __init__(self, x, y, is_bosslayer = False):
        super().__init__(x, y, is_bosslayer)
        self.health = 1
        self.pixel =  Back.YELLOW+' '+Style.RESET_ALL
        self.score = 100
    
class MediumBrick(Brick):

    def __init__(self, x, y, is_bosslayer = False):
        super().__init__(x, y, is_bosslayer)
        self.health = 2
        self.pixel =  Back.CYAN+' '+Style.RESET_ALL
        self.score = 200
            
class HardBrick(Brick):

    def __init__(self, x, y, is_bosslayer = False):
        super().__init__(x, y, is_bosslayer)
        self.health = 3
        self.pixel =  Back.MAGENTA+' '+Style.RESET_ALL
        self.score = 300
    
class UnbreakableBrick(Brick):

    def __init__(self, x, y, is_bosslayer = False):
        super().__init__(x,y, is_bosslayer)
        self.health = -1
        self.pixel =  Back.WHITE+' '+Style.RESET_ALL
        self.score = 50
        
class SuperBrick(Brick):

    def __init__(self, x, y, is_bosslayer = False):
        super().__init__(x,y, is_bosslayer)
        self.health = 1
        self.pixel =  Back.BLUE+' '+Style.RESET_ALL
        self.score = 400

    def reduce_health(self, forced=True):
        self.health = 0
        return self.score