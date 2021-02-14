from getinput import get_input

class Paddle():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.height = 1
        self.width = 10

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_dimension(self, height=1, width=10):
        self.height = height
        self.width = width

    def move(self, board):
        char = get_input()
        if(char == 'd'):
            if((self.x+self.width-1) < (board.cols-1)):
                self.x = self.x+1
        elif(char == 'a'):
            if(self.x > 0):
                self.x = self.x-1
        return char