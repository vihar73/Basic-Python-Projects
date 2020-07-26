# Tic-Tac-Toe
board = [['','',''],
         ['','',''],
         ['','','']]
def reinitialize(board):
    board = [['','',''],
             ['','',''],
             ['','','']]
    return board

def printboard(board):
    for line in board:
        for num in line:
            if num == "":
                print(" ", end = " | ")
            else:
                print(num, end = " | ")
        print("")

def wingame(board):
    #row win
    for line in board:
        if line[0] == line[1] == line[2] and line[0] != '':
            return line[0] #row win
    #column win
    for r in range(len(board)):
        if board[0][r] == board[1][r] == board[2][r] and board[0][r] != '':
            return board[0][r] #column win
    #diagonal win
        for c in range(len(board[r])):
            if r == c:
                if board[r][c] != board[1][1]:
                    return None
            if r + c ==2:
                if board[r][c] != board[1][1]:
                    return None
        if board [1][1] != '':
            return board[1][1] #diagonal win
    return None #no win

def validentry(board):
    validentry = []
    imap = {'(0,0)':7, '(0,1)':8, '(0,2)':9,
            '(1,0)':4, '(1,1)':5, '(1,2)':6,
            '(2,0)':1, '(2,1)':2, '(2,2)':3}
    for r in range(len(board)):
        for c in range(len(board[r])): 
            if board[r][c] == '':
                key = '(' + str(r) + ',' + str(c) + ')'
                validentry.append(imap[key])
    return validentry
count = 0           
def playgame(board, turn = 'x'):
    imap = {'7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2)}

    #turn = 'x'
    inp_str = input('Play ' + turn +': ')
    
    if inp_str.lower() == 'end' or inp_str.lower() == 'exit':
        print('Game ended')
        return None
        
    inp = int(inp_str)
    
    if inp not in range(1,10):
        print("Enter number between 1-9")
    val_list = validentry(board)
        
    if len(val_list) == 0:
        print("Game finished. Winner is ", wingame(board))
        playagain = input("Press P to play again, any other key to exit:")
        print('b')
        if playagain.lower() == 'p':
            reinitialize(board)
            playgame(board)
        else:
            return None
        
    if inp not in val_list:
        print("Enter a valid number")
        print(val_list)
        playgame(board, turn = turn)
    else:
        board[imap[inp_str][0]][imap[inp_str][1]] = turn
        printboard(board)
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
            
        if wingame(board):
            print ('Winner is :', wingame(board))
            print('a')
            playagain = input("Press P to play again, any other key to exit:")
            if playagain.lower() == 'p':
                reinitialize(board)
                playgame(board)
            else:
                return None
            
        playgame(board, turn = turn)
 
#welcome message
print("Welcome to Tic-Tac-Toe, this is a 2 player game - inputs are based on traditional num pads")
print("7 | 8 | 9 |")
print("4 | 5 | 6 |")
print("1 | 2 | 3 |")
input("Press any key to play:")
playgame(board)
