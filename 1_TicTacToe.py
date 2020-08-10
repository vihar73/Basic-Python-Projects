# Tic-Tac-Toe
board1 = [['','',''],
         ['','',''],
         ['','','']]

def reinitialize(board):
    board = [['','',''],
             ['','',''],
             ['','','']]
    return board

'''Helper - Print the board'''
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
    if board[0][0] == board[1][1] ==board[2][2]:
        if board[1][1] != '':
            return board[1][1] #diagonal win

    if board[0][2] == board[1][1] ==board[2][0]:
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
        dupboard.append(item[:])
    return dupboard

'''Minimax algorithm'''
def minimax(board, turn, depth = 0, flag = 0):
    deepboard = copyboard(board)

    imap = {'7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2)}

    if wingame(deepboard):
        return {'scr':(10 - depth),'move': None} if wingame(deepboard) == 'x' else {'scr':(-10 + depth),'move': None}
    elif len(validentry(deepboard)) == 0:
        #print("draw??", move, turn, 0)
        return {'scr':(0),'move': None}
    '''
    elif move in validentry(deepboard):
        move_str = str(move)
        deepboard[imap[move_str][0]][imap[move_str][1]] = turn

        if wingame(deepboard):
            return (10 - depth) if wingame(deepboard) == 'x' else (-10 + depth)
        elif len(validentry(deepboard)) == 0:
            #print("draw??", move, turn, 0)
            return (0-depth)
    '''
    if turn == 'x':
        best = {'scr':-400000, 'move': None}
    else:
        best = {'scr':400000, 'move': None}

    for move in validentry(deepboard):
        deep_deepboard = []
        if flag == 1:
           deep_deepboard = copyboard(deepboard)
        move_str = str(move)
        deepboard[imap[move_str][0]][imap[move_str][1]] = turn
        printboard(deepboard)
        turn = switchturns(turn)
        value = minimax(deepboard, turn = turn, depth = depth+1)
        if deep_deepboard != []:
            deepboard = copyboard(deep_deepboard)
        print(switchturns(turn), move, value, best)

        value['move'] = move

        if turn == 'x':
            if value['scr'] < best['scr']:
                best = value
        else:
            if value['scr'] > best['scr']:
                best = value
        #print(best)
    return best

    '''
    elif turn == 'o':
        best = {'scr':400000, 'move': None}
        for move in validentry(deepboard):
            move_str = str(move)
            deepboard[imap[move_str][0]][imap[move_str][1]] = turn
            turn = switchturns(turn)
            value = minimax(deepboard, turn = turn, depth = depth+1)

        if value['scr'] < best['scr']:
             best['scr'] = value['scr']
             best['move'] = value['move']
        return best
     '''
'''Making max-score move from minimax'''
def computemove(board):
    #print(board,0)
    if len(validentry(board)) == 0:
        return None
    #mv_scr = []
    mv_scr = minimax(board, turn = 'x', flag = 1)
    print(mv_scr)
    return mv_scr['move']
    #deepboard = board
    '''
    for move in validentry(board):
        scr = minimax(board,move)
        mv_scr.append((move, scr))
    print(mv_scr)
        #printboard(board)
    #scr = max(pair[1] for pair in mv_scr)

    for item in mv_scr:
        if item[1] == None:
            mv_scr.remove(item)
    for item1 in mv_scr:
        if item1[1] == max(pair[1] for pair in mv_scr):
            return item1[0]
    '''
'''Playing the game'''
def playgame(board, turn = 'o'):
    #print(wingame(board))
    if wingame(board):
        print ('Winner is ://', wingame(board))
        return wingame(board)

    val_list = validentry(board)
    if len(val_list) == 0:
        print("Game finished. Winner is //", wingame(board))
        return None
    imap = {'7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2)}

    if turn == 'x':
        print("Bot move")
        inp = computemove(board)
        inp_str = str(inp)
    else:
        inp_str = input('Play ' + turn +': ')
        if inp_str.lower() == 'end' or inp_str.lower() == 'exit':
            print('Game ended??')
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
