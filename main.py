from board import Board

board = Board(paddle)

while(True):
    check = board.paddle.move(board)
    if(check == 'q'):
        break
    board.render()