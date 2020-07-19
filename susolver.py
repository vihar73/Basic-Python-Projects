
sudoku = [[7,8,0,4,0,0,1,2,0], [6,0,0,0,7,5,0,0,9], [0,0,0,6,0,1,0,7,8],
          [0,0,7,0,4,0,2,6,0], [0,0,1,0,5,0,9,3,0], [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2], [1,2,0,0,0,7,4,0,0], [0,4,9,2,0,6,0,0,7]]
g = 3

def pprintsud(sud):
    for i in range (len(sud)):
        if i % g == 0: #and i != 0:
            print ("  ----------------------- ")
    
        for j in range(len(sud[i])):
            
            if j % g == 0: #and j != 0:
                print(" |",end = "")
  
            if sud[i][j] ==0:
                print(" .", end = "")
            else:
                print(" ", end = "")
                print(sud[i][j], end = "")
       
        print(" |")
    print ("--------------------------")

def findblank(sud):
    for i in range (len(sud)):
        for j in range(len(sud[i])):
            if sud[i][j] == 0:
                return (i, j)
    return None

def checkval(sud, num, i, j):
    if num in sud[i]:
        return False #row validation
        if num in (sud[i][a] for a in range(len(sud))):
            return False #column validation
            x1 = g * (i // g)
            y1 = g * (j // g)
            for x in range(x1,x1+g):
                for y in range(y1,y1+g):
                    if sud[x][y] == num:
                        print("bf")
                        return False #box validation
    else:
        return True

pprintsud(sudoku)

class ssolve():
    counter = 0
    def solve(sud):
        blank = findblank(sud)
        if not blank:
            return True
        else:
            A, B = blank
            #print(2)
            for num in range(len(sud)):
                if checkval(sud, num+1, A, B):
                    sud[A][B] = num+1
                    #print(3)
                    if ssolve.solve(sud):
                        ssolve.counter = ssolve.counter + 1
                        return True
                    else:
                        sud[A][B] = 0
            return False

    def count(sud):
        if ssolve.solve(sud):
            return ssolve.counter

ssolve.solve(sudoku)
print ("Solved sudoku (",ssolve.count(sudoku),"tries):")

pprintsud(sudoku)

            
            
