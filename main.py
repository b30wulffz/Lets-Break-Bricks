from board import Board

board = Board()

# In order to follow coordinate system, (x,y) needs to be written in [y][x] format, where y grows downwards.

while(True):
    check = board.paddle.move(board)
    if(check == 'q'):
        break
    board.render()

# board.ball.move(board)