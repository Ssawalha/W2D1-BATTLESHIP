BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'


class GameBoard:
    def __init__(self, width=5, height=5):
        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid = grid
                        #ie(3,4)
    def __getitem__(self, indices):
        print('Getting item at index: ', indices)
        col_index, row_index = indices #(unpack notation) we are setting index to a tuple of (col_index, row_index)
        return self.grid[row_index - 1][col_index - 1]

    def __setitem__(self, indices, value):
        print('Setting item at index: ', indices, 'to', value)
        row_index, col_index = indices
        self.grid[row_index - 1][col_index - 1] = value
    
    def __bool__(self): #Checks if any ships are still on the board
        for row in self.grid:
            for col in row:
                if col == 'S':
                    return True
        return False

    def __str__(self): #(how you want things to be represented)          prints values as string
        for element in self.board: #self.grid?
            print (element)
    
    def __repr__(self): #similar to __str__ google what they mean  
        for element in self.board:
            print (element)

if __name__ == "__main__":
    pass

    board = GameBoard()
    board[2,3] = 'S'
    if board:
        print('Board was True!')
    else:
        print('Board was False!')
    x = board[2,3]
    print (x)
    print (board.grid)
