import GameConsole as console
BOARD_ROWS = 6
BOARD_COLUMN = 7
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
player = True
lastColumnPlay = "A"
board = []
for y in range (BOARD_COLUMN):
    boardColumn = []
    boardColumn.append(alphabet[y])
    for x in range (BOARD_ROWS):
        boardColumn.append("0")
    board.append(boardColumn)
print(board)

def clearBoard():
    for elements in (board):
        board[elements].pop
    
def canPlay(columnIndex): #return the cell free in this column or -1 if no cell free
    for i in range (len(boardColumn)):
        if board[columnIndex][i] == "0":
            return True
    return False

def playWhatRow(columnIndex): #return the cell free in this column 
    for i in range (len(boardColumn)):
        if board[columnIndex][i] == "0":
            return i

def whoWillPlay(whoPlay):
    if whoPlay == "RED":
        whoPlay = "YELLOW"
    else:
        whoPlay = "RED"
    return(whoPlay)

def findColumnIndex(letter):
    for c in range (len(alphabet)):
        if letter == alphabet[c]:
            return c 

def play(isRed, columnIndex): 
    boardCol = []
    global lastColumnPlay
    for i in range (len(board[columnIndex])):
        if i < playWhatRow(columnIndex):
            boardCol += board[columnIndex][i]
        elif isRed and i == playWhatRow(columnIndex) and canPlay(columnIndex):
            boardCol.append("R")
            lastColumnPlay = board[columnIndex][0]
        elif not isRed and i == playWhatRow(columnIndex) and canPlay(columnIndex):
            boardCol.append("Y")
            lastColumnPlay = board[columnIndex][0]
        else:
            boardCol.append("0")
    board[columnIndex] = boardCol

def getBoardStatus(): #Return the board status
    if isBoardFull() == True :
        boardStatus = "BOARD_FULL"    #BOARD_FULL The board is full, but no winner
        console.boardFull()
    elif playerWonRow(True) or playerWonColumn(True) or playerWonDiagonal(True):
        boardStatus = "RED_WON"    #RED_WON RED player has won
        console.redWon()
    elif playerWonRow(False) or playerWonColumn(False) or playerWonDiagonal(False):
        boardStatus = "YELLOW_WON"    #YELLOW_WON YELLOW player has won
        console.yellowWon()
    else:
        boardStatus = "ON_PROGRESS"    #ON_PROGRESS No winner for now
    return boardStatus

def playerWonRow(isRed):
    for i in range (len(board)):
        rednonestop = 0
        yellownonestop = 0
        for j in range (len(board[0])):
            if board[j][i] == "R" and isRed:
                rednonestop +=1
            elif board[j][i] == "Y" and not isRed:
                yellownonestop += 1
            else:
                rednonestop = 0
                yellownonestop = 0
            if rednonestop >= 4 or yellownonestop >= 4:
                return True
    return False

def playerWonDiagonal(isRed):
    global lastColumnPlay
    lastX = 0
    lastY = 0
    for letter in range (len(alphabet)):
        if alphabet[letter] == lastColumnPlay:
            lastX = letter
    for i in range (len(board[lastX])):
        if  board[lastX][i] == "R" or board[lastX][i] == "Y":
            lastY = i
    diag1=isSameSymbol(lastX-1,lastY-1,isRed) and isSameSymbol(lastX-2,lastY-2,isRed) and isSameSymbol(lastX-3,lastY-3,isRed)
    diag2=isSameSymbol(lastX-1,lastY-1,isRed) and isSameSymbol(lastX-2,lastY-2,isRed) and isSameSymbol(lastX+1,lastY+1,isRed)
    diag3=isSameSymbol(lastX-1,lastY-1,isRed) and isSameSymbol(lastX+2,lastY+2,isRed) and isSameSymbol(lastX+1,lastY+1,isRed)
    diag4=isSameSymbol(lastX+3,lastY+3,isRed) and isSameSymbol(lastX+2,lastY+2,isRed) and isSameSymbol(lastX+1,lastY+1,isRed)
    diag5=isSameSymbol(lastX-1,lastY+1,isRed) and isSameSymbol(lastX-2,lastY+2,isRed) and isSameSymbol(lastX-3,lastY+3,isRed)
    diag6=isSameSymbol(lastX-1,lastY+1,isRed) and isSameSymbol(lastX-2,lastY+2,isRed) and isSameSymbol(lastX+1,lastY-1,isRed)
    diag7=isSameSymbol(lastX-1,lastY+1,isRed) and isSameSymbol(lastX+2,lastY-2,isRed) and isSameSymbol(lastX+1,lastY-1,isRed)
    diag8=isSameSymbol(lastX+3,lastY-3,isRed) and isSameSymbol(lastX+2,lastY-2,isRed) and isSameSymbol(lastX+1,lastY-1,isRed)
    return diag1 or diag2 or diag3 or diag4 or diag5 or diag6 or diag7 or diag8

def isSameSymbol(X, Y, isRed):
    if X >= 0 and X <= BOARD_ROWS-1 and Y >= 0 and Y <= BOARD_COLUMN-1:
        if board[X][Y] == "R" and isRed:
            return True
        elif board[X][Y] == "Y" and not isRed:
            return True
    return False

def playerWonColumn(isRed):
    for i in range (len(board)):
        rednonestop = 0
        yellownonestop = 0
        currentColumn = board[i]
        for j in range (len(board[0])):
            if currentColumn[j] == "R" and isRed:
                rednonestop +=1
            elif currentColumn[j] == "Y" and not isRed:
                yellownonestop += 1
            else:
                rednonestop = 0
                yellownonestop = 0
            if rednonestop >= 4 or yellownonestop >= 4:
                return True
    return False

def isBoardFull():
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[j][i] == "0":
                return False
    return True

def getIndexOfLetter(letter):
    for index in range (BOARD_COLUMN):
        if board[index][0] == letter:
            return index

console.welcome()
while getBoardStatus() == "ON_PROGRESS":
    player = whoWillPlay(player)
    if player == "YELLOW":
        play(False, getIndexOfLetter(str(input("Player Yellow, enter column to play: ")).upper()))
    else:
        play(True,  getIndexOfLetter(str(input("Player Red, enter column to play: ")).upper()))
    console.printBoard(board)