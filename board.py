from os import system

class Board():

    def __init__(self, paddle, bricks=[], balls=[]):
        self.cols = 80
        self.rows = 40
        self.paddle = paddle
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]
        self.render()

    def render(self):

        system('clear')
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]

        # render paddle
        for row in range(self.paddle.y,  self.paddle.y+self.paddle.height):
            for col in range(self.paddle.x, self.paddle.x+self.paddle.weight):
                self.board[row][col] = '*'
        
        print("\n".join(["".join(row) for row in self.board]))
