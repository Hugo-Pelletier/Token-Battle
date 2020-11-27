import GameConsole as console
BOARD_ROWS = 6
BOARD_COLUMN = 7
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
player = True
    
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

def play( isRed, columnIndex): 
    boardCol = []
    for i in range (len(board[columnIndex])):
        if i < playWhatRow(columnIndex):
            boardCol += board[columnIndex][i]
        elif isRed and i == playWhatRow(columnIndex) and canPlay(columnIndex):
            boardCol.append("R")
        elif not isRed and i == playWhatRow(columnIndex) and canPlay(columnIndex):
            boardCol.append("Y")
        else:
            boardCol.append("0")
    board[columnIndex] = boardCol

def getBoardStatus(): #Return the board status
    if isBoardFull() == True :
        boardStatus = "BOARD_FULL"    #BOARD_FULL The board is full, but no winner
        console.boardFull()
    elif playerWonRow(True):
        boardStatus = "RED_WON"    #RED_WON RED player has won
        console.redWon()
    elif playerWonRow(False):
        boardStatus = "YELLOW_WON"    #YELLOW_WON YELLOW player has won
        console.yellowWon()
    else:
        boardStatus = "ON_PROGRESS"    #ON_PROGRESS No winner for now
        print("Test")
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