from getinput import get_input

class Paddle():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.height = 2
        self.weight = 10

    def move(self):
        char = get_input()
        if(char == 'd'):
            self.x = self.x+1
        elif(char == 'a'):
            self.x = self.x-1
        return char