from board import Board

board = Board()

while(True):
    check = board.paddle.move(board)
    if(check == 'q'):
        break
    board.render()