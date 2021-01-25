import copy
import random


# 1 --> x 
# 0 --> 0
# None --> Nothing
# x plays first
# player places from 0 to 2 

def printTable(matrix):  
    print('''
            {0}     {1}     {2}

            {3}     {4}     {5}

            {6}     {7}     {8}
          '''.format(matrix[0][0],matrix[0][1],matrix[0][2],matrix[1][0],matrix[1][1],matrix[1][2],matrix[2][0],matrix[2][1],matrix[2][2]))

def checkifWin(table, who):  
    for x in range(3):
        if table[x][0] == who and table[x][1] == who and table[x][2] == who:
            return 1
    for y in range(3):
        if table[0][y] == who and table[1][y] == who and table[2][y] == who:
            return 1
    if table[0][0] == who and table[1][1] == who and table[2][2] == who:
        return 1

    if table[0][2] == who and table[1][1] == who and table[2][0] == who:
        return 1
    return 0

def availablePositions(table,who):
    availablePos = []
    for x in range(len(table)):   
        for y in range(len(table[x])):   
            if table[x][y] == None:
                newMatrix = [[],[]]
                newMatrix[0] = copy.deepcopy(table)
                newMatrix[0][x][y] = who
                newMatrix[1] = [x,y]
                availablePos.append(newMatrix)
    return availablePos

def botMove(table, botPlaying,playerPlaying):
    # check if the bot can wins 
    avPosBot = availablePositions(table,botPlaying)
    for posBot in avPosBot:
        if checkifWin(posBot[0],botPlaying):
            table[posBot[1][0]][posBot[1][1]] = botPlaying
            return 1
    # check if the player can win to counter him
    avPosPlayer = availablePositions(table,playerPlaying)
    for posPlayer in avPosPlayer:
        if checkifWin(posPlayer[0],playerPlaying):
            table[posPlayer[1][0]][posPlayer[1][1]] = botPlaying
            return 1
    # else place a random spot
    place = avPosBot[random.randrange(len(avPosBot))][1]
    table[place[0]][place[1]] = botPlaying
    return 0

def main():
    currentPlaying = 1
    botPlaying = 0
    playerPlaying = 1
    table = [[None,None,None],
            [None,None,None],
            [None,None,None]]  

    while True:
        printTable(table)       
        if currentPlaying == botPlaying: 
            print("Bot turn")
            botMove(table,botPlaying,playerPlaying)
        else:
            print("Player turn")
            playerFinished = False
            while not playerFinished:
                try:
                    place = input("Where you want to place X,Y:").split(',')
                    if len(place) == 2:
                        if table[int(place[0])][int(place[1])] == None:
                            table[int(place[0])][int(place[1])] = playerPlaying
                            playerFinished = True      
                        else:
                            print("Place not available")      
                    else:
                        print("Input error")
                except ValueError:
                    print("\n {0} \n".format(ValueError))          
        if checkifWin(table,currentPlaying):
            printTable(table)   
            print("Player {0} won".format(currentPlaying))
            exit(1)
        currentPlaying = int(not currentPlaying)

if __name__ == '__main__':
    main()
    