
import gameboard as g
import view as v

BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'

#first thing we want to setup the board from scratch every game:
#computer should have random placement of ships

def start():
    
    p1_board = g.GameBoard()
    p2_board = g.GameBoard()
    
    turn = 0
    row = 0
    col = 0
    # player_selection=[row,col]

    p1_ships = ['S','S','S','S']
    p2_ships = ['S','S','S','S']

    while p1_ships != [] and p2_ships != []:
        if turn % 2 == 0:
            #os.system('clear')
            print('P1s Turn')
            print('P1s Board:')
            v.show_board(p1_board)
            if p1_ships == []:
                print('Select Target')
                row = int(input('Enter row num (top row = 1): '))
                col = int(input('Enter col num (leftmost col  = 1): '))
            
            else:
                print('Place A Ship')
                row = int(input('Enter row num (top row = 1): '))
                col = int(input('Enter col num (leftmost col  = 1): '))
                if p1_board[row, col] == ' ':
                    p1_board[row, col] = p1_ships.pop()

                else:
                    print('Please choose another location.') 
                    row = int(input('Enter row num (top row = 1): '))
                    col = int(input('Enter col num (leftmost col  = 1): '))
                    if p1_board[row, col] == ' ':
                        p1_board[row, col] = 'S'         
            v.show_board(p1_board)    
            print('Ending turn')
            turn += 1


        if turn % 2 != 0:
            #os.system('clear')
            print('P2s Turn')
            print('P2s Board:')
            v.show_board(p2_board)
            if p2_ships == []:
                print('Select Target')
                row = int(input('Enter row num (top row = 1): '))
                col = int(input('Enter col num (leftmost col  = 1): '))
            
            else:
                print('Place A Ship')
                row = int(input('Enter row num (top row = 1): '))
                col = int(input('Enter col num (leftmost col  = 1): '))
                if p2_board[row, col] == ' ':
                    p2_board[row, col] = p2_ships.pop()
                else:
                    print('Please choose another location.') 
                    row = int(input('Enter row num (top row = 1): '))
                    col = int(input('Enter col num (leftmost col  = 1): '))
                    if p2_board[row, col] == ' ':
                        p2_board[row, col] = 'S'         
            v.show_board(p2_board)
            print('Ending turn')    
            turn += 1
    
    
    
    
    # p1_board[]



if __name__ == "__main__":
    testlst1 = [['a','b']]
    testlst2 = []
    testlst2 = testlst1.pop()
    print(testlst1)
    start()




#then prompt user for an index
#check if hit or miss
#update board with hit or miss
#tell user whether hit or miss

#computer's turn, tell user where the computer tried to hit, check if hit or miss
#update user's board
#take input from user for next turn


