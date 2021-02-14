from board import Board
from paddle import Paddle

paddle = Paddle(4,4)
board = Board(paddle)

while(True):
    check = paddle.move()
    if(check == 'q'):
        break
    board.render()