# Tic-Tac-Toe
board1 = [['','',''],
         ['','',''],
         ['','','']]

def reinitialize(board):
    board = [['','',''],
             ['','',''],
             ['','','']]
    return board

'''Print the board'''
def printboard(board):
    for line in board:
        for num in line:
            if num == "":
                print(" ", end = " | ")
            else:
                print(num, end = " | ")
        print("")
    print("---------")

'''Check winnner on board'''
def wingame(board):
    #row win
    for line in board:
        if line[0] == line[1] == line[2]:
            if line[0] != '':
                return line[0] #row win
    #column win
    for r in range(len(board)):
        if board[0][r] == board[1][r] == board[2][r]:
            if board[0][r] != '':
                return board[0][r] #column win
    #diagonal win
    '''
    for r1 in range(len(board)):
        for c1 in range(len(board[r1])):
            if r1 == c1:
                if board[r1][c1] != board[1][1]:
                    return None
                elif board [1][1] != '':
                    return board[1][1] #diagonal win
            if r1 + c1 ==2:
                if board[r1][c1] != board[1][1]:
                    return None
                elif board [1][1] != '':
                    return board[1][1] #diagonal win
    '''
    if board[0][0] == board[1][1] ==board[2][2]:
        if board[1][1] != '':
            return board[1][1] #diagonal win
        
    if board[0][2] == board[1][1] ==board[0][2]:
        if board[1][1] != '':
            return board[1][1] #diagonal win
    return None #no win

'''Helper - check valid entries on board'''
def validentry(board):
    validentry = []
    omap = {'(0,0)':7, '(0,1)':8, '(0,2)':9,
            '(1,0)':4, '(1,1)':5, '(1,2)':6,
            '(2,0)':1, '(2,1)':2, '(2,2)':3}
    for r in range(len(board)):
        for c in range(len(board[r])): 
            if board[r][c] == '':
                key = '(' + str(r) + ',' + str(c) + ')'
                validentry.append(omap[key])
    return validentry

'''Helper - switch turns'''
def switchturns(turn):
    if turn == 'x':
        return 'o'
    else:
        return 'x'

'''Helper - copy board'''
def copyboard(board):
    dupboard = []
    for item in board:
        dupboard.append(item)
    return dupboard

'''Minimax algorithm'''
def minimax(deepboard, move, turn = 'x', depth = 0):
    #deepboard = copyboard(board)
    if wingame(deepboard):
        if wingame(deepboard) == 'x':
            print('win??')
            return (10-depth)
        else:
            print("lose??")
            return (-10+depth)
    if len(validentry(deepboard)) == 0:
        print("draw??")
        return (0-depth)
            
    imap = {'7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2)}
    if move in validentry(deepboard):
        move_str = str(move)
        deepboard[imap[move_str][0]][imap[move_str][1]] = turn
        print(depth)
        
        for rem_move in validentry(deepboard):
            turn = switchturns(turn)
            print("turn switched", turn)
            minimax(deepboard, rem_move, turn = turn, depth = depth+1)
        
'''Making max-score move from minimax'''
def computemove(board):
    deepboard = copyboard(board)
    if len(validentry(deepboard)) == 0:
        return None
    mv_scr = []
    #deepboard = board
    for move in validentry(deepboard):
        scr = minimax(deepboard,move)
        mv_scr.append((move, scr))
        printboard(board)
        printboard(deepboard)
    #scr = max(pair[1] for pair in mv_scr)
    print(mv_scr)
    for item in mv_scr:
        if item[1] == None:
            mv_scr.remove(item)
        if item[1] == max(pair[1] for pair in mv_scr):
            return item[0]

'''Playing the game'''
def playgame(board, turn = 'o'):
    #print(wingame(board))
    if wingame(board):
        print ('Winner is :', wingame(board))
        return wingame(board) 
    
    val_list = validentry(board)
    if len(val_list) == 0:
        print("Game finished. Winner is ", wingame(board))
        return None
    
    if turn == 'x':
        print("Bot move")
        inp = computemove(board)        
    else:
        imap = {'7':(0,0), '8':(0,1), '9':(0,2),
                '4':(1,0), '5':(1,1), '6':(1,2),
                '1':(2,0), '2':(2,1), '3':(2,2)}
        inp_str = input('Play ' + turn +': ')
        if inp_str.lower() == 'end' or inp_str.lower() == 'exit':
            print('Game ended')
            return None
        inp = int(inp_str)

    if inp in val_list:
        board[imap[inp_str][0]][imap[inp_str][1]] = turn
        printboard(board)
        turn = switchturns(turn)
    else:
        print("Enter a valid number")
        print(val_list)
    
    playgame(board, turn = turn)

#welcome message
print("Welcome to Tic-Tac-Toe, this is a 2 player game - inputs are based on traditional num pads")
print("7 | 8 | 9 |")
print("4 | 5 | 6 |")
print("1 | 2 | 3 |")
#input("Press enter to play:")
playgame(board1)
