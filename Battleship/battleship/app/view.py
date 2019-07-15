import gameboard as g

#We want to display the board of Player 1

def show_board(board):
#     if board == 'p1_board':
#         print('P1s Turn')
#         print('P1s Board:')
#     elif board == 'p2_board':
#         print('P2s Turn')
#         print('P2s Board:')
    for row in board.grid:
        print (row)


if __name__ == "__main__":
    pass