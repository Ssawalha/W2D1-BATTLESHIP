board = GameBoard()
board[2,3] = 'S'
if board:
    print('Board was True!')
else:
    print('Board was False!')
x = board[2,3]
print (x)
print (board.grid)