from colorama import Fore, Back, Style 
from utils import Utils

class Bullet():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.height = 1
        self.width = 1
        self.velocity_y = -1
        
        self.pixel = Back.RED+' '+Style.RESET_ALL
        self.avoid_pixel = [Back.RED+Fore.WHITE+str(i)+Style.RESET_ALL for i in range(1,8)]
        self.avoid_pixel.append(self.pixel)
    
    def move(self, board):
        self.y += self.velocity_y

        top_coordinates = Utils.get_coordinates(self, "top")

        for coord in top_coordinates:
            if coord['y'] <= 0:
                Utils.destroy(self, board.paddle.bullets)
                return True
            elif coord['y'] > 0 and coord['x']>=0 and coord['x']<board.cols:
                if(board.board[coord['y']-1][coord['x']] != board.bg_pixel and board.board[coord['y']-1][coord['x']] not in self.avoid_pixel):
                    Utils.destroy(self, board.paddle.bullets)
                    board.brick_detect_and_remove(coord['x'], coord['y']-1)
                    return True
        return False