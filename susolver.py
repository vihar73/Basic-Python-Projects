'''
sudoku = [[2,0,0,3,0,0,0,0,0],[8,0,4,0,6,2,0,0,3],[0,1,3,8,0,0,2,0,0],
          [0,0,0,0,2,0,3,9,0],[5,0,7,0,0,0,6,2,1],[0,3,2,0,0,6,0,0,0],
          [0,2,0,0,0,9,1,4,0],[6,0,1,2,5,0,8,0,9],[0,0,0,0,0,1,0,0,2]]

sudoku = [[0,2,0,6,0,8,0,0,0],[5,8,0,0,0,9,7,0,0],[0,0,0,0,4,0,0,0,0],
          [3,7,0,0,0,0,5,0,0],[6,0,0,0,0,0,0,0,4],[0,0,8,0,0,0,0,1,3],
          [0,0,0,0,2,0,0,0,0],[0,0,9,8,0,0,0,3,6],[0,0,0,3,0,6,0,9,0]]
'''
sudoku = [[0,2,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0,3],[0,7,4,0,8,0,0,0,0],
          [0,0,0,0,0,3,0,0,2],[0,8,0,0,4,0,0,1,0],[6,0,0,5,0,0,0,0,0],
          [0,0,0,0,1,0,7,8,0],[5,0,0,0,0,9,0,0,0],[0,0,0,0,0,0,0,4,0]]
g = 3

def pprintsud(sud):
    dash = (g * 8) - 1
    for i in range (len(sud)):
        if i % g == 0: #and i != 0:
            print (" .","-" * dash,". ",sep = "")

        for j in range(len(sud[i])):

            if j % g == 0: #and j != 0:
                print(" |",end = "")

            if sud[i][j] ==0:
                print(" .", end = "")
            else:
                print(" ", end = "")
                print(sud[i][j], end = "")

        print(" |")
    print (" .","-" * dash,". ",sep = "")

def findblank(sud):
    for i in range (len(sud)):
        for j in range(len(sud[i])):
            if sud[i][j] == 0:
                return (i, j)
    return None

def checkval(sud, num, i, j):
    if num not in sud[i]:                                    #row validation
        if num not in (sud[a][j] for a in range(len(sud))):  #column validation
            r1 = g * (i // g)                                #box validation
            c1 = g * (j // g)
            #box = []
            if num not in (sud[r][c] for r in range(r1,r1+g) for c in range(c1,c1+g)):
                 return True                                 #all validation
    else:
        return False

def printblock(sud, i ,j):
    r1 = g * (i//g)
    c1 = g * (j//g)
    for row in range(r1,r1+g):
        for col in range(c1,c1+g):
            print(sud[row][col], end = "")
        print("")

pprintsud(sudoku)

class ssolve():
    counter = 0
    def solve(sud):
        blank = findblank(sud)
        if not blank:
            return True
        else:
            A, B = blank
            for num in range(len(sud)):
                if checkval(sud, num+1, A, B):
                    sud[A][B] = num+1
                    if ssolve.solve(sud):
                        #ssolve.counter = ssolve.counter + 1
                        return True
                    else:
                        ssolve.counter = ssolve.counter + 1
                        sud[A][B] = 0
            return False

    def count(sud):
        if ssolve.solve(sud):
            return ssolve.counter

ssolve.solve(sudoku)
print ("Solved sudoku (",ssolve.count(sudoku),"tries):")

pprintsud(sudoku)
