from colorama import Fore, Back, Style 
from utils import Utils

class Bomb():
    def __init__(self, x, y):
        self.velocity_y = 1

        self.x = x
        self.y = y

        self.height = 1
        self.width = 1

        self.pixel =  Back.BLUE+Fore.RED+'*'+Style.RESET_ALL
        self.avoid_pixel = [Back.RED+Fore.WHITE+str(i)+Style.RESET_ALL for i in range(1,8)]
        self.avoid_pixel += [self.pixel, Back.RED+' '+Style.RESET_ALL]

    def move(self, board):
        self.y += self.velocity_y

        bottom_coordinates = Utils.get_coordinates(self, "bottom")
        for coord in bottom_coordinates:
            if coord['y'] >= board.rows:
                Utils.destroy(self, board.boss.bombs)
                return True
            elif coord['y'] < board.rows and coord['x']>=0 and coord['x']<board.cols:
                if(board.board[coord['y']][coord['x']] != board.bg_pixel and board.board[coord['y']][coord['x']] not in self.avoid_pixel):
                    # paddle detected
                    if(coord['y'] == board.paddle.y):
                        Utils.destroy(self, board.boss.bombs)
                        board.lives -= 1
                        return True
        return False