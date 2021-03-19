from colorama import Fore, Back, Style 
from bomb import Bomb
from brick import EasyBrick, MediumBrick, HardBrick
import random

class Boss():

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.height = 3
        self.width = 18

        self.health = 10
        self.max_health = 10
        self.bombs = []

        self.layer_factor = 200
    
    def reduce_health(self):
        if self.health > 0:
            self.health -= 1

    def render(self, board):
        row = self.y
        mid = (self.x + self.x+self.width) // 2

        # render boss
        row = self.y
        board.board[row][self.x] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+1] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+2] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+self.width-3] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+self.width-2] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+self.width-1] = Back.YELLOW+' '+Style.RESET_ALL

        row = self.y+1
        for col in range(mid-3, mid+3):
            board.board[row][col] = Back.GREEN+' '+Style.RESET_ALL
        
        if self.health > 0:
            board.board[row][mid-2] = Back.GREEN+Fore.RED+'O'+Style.RESET_ALL
            board.board[row][mid+1] = Back.GREEN+Fore.RED+'O'+Style.RESET_ALL
        else:
            board.board[row][mid-2] = Back.GREEN+Fore.RED+'X'+Style.RESET_ALL
            board.board[row][mid+1] = Back.GREEN+Fore.RED+'X'+Style.RESET_ALL
        
        board.board[row][self.x] = Back.YELLOW+' '+Style.RESET_ALL
        board.board[row][self.x+self.width-1] = Back.YELLOW+' '+Style.RESET_ALL

        row = self.y+2
        for col in range(self.x, self.x+self.width):
            board.board[row][col] = Back.BLUE+' '+Style.RESET_ALL
        
        # render bombs
        if(board.ticks % 50 == 0 and self.health>0):
            self.bombs.append(Bomb(random.randint(self.x, self.x+self.width-1), 3))
        
        for bomb in self.bombs:
            for row in range(bomb.y, bomb.y+bomb.height):
                for col in range(bomb.x, bomb.x+bomb.width):
                    board.board[row][col] = bomb.pixel
            bomb.move(board)
        
        # spawn brick layer
        if self.health+self.layer_factor == 205 or self.health+self.layer_factor == 102:
            if self.layer_factor > 0:
                self.layer_factor -= 100
            x = self.x
            y = self.y + self.height
            for x_val in [x, x+6, x+12]:
                brick = random.choice([EasyBrick(x_val, y, True), MediumBrick(x_val, y, True), HardBrick(x_val, y, True), ])
                board.bricks.append(brick)