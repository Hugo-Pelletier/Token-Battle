import GameConsole as console
BOARD_ROWS = 6
BOARD_COLUMN = 7
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
boardStatus = "ON_PROGRESS"
whoplay = "RED"
    
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

def playWhatRow(columnIndex): #return the cell free in this column or -1 if no cell free
    for i in range (len(boardColumn)):
        if board[columnIndex][i] == "0":
            return i

def whoPlay():
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
        elif not isRed and i == playWhatRow(columnIndex) and i == canPlay(columnIndex):
            boardCol.append("Y")
        else:
            boardCol.append("0")
    board[columnIndex] = boardCol

def getBoardStatus(): #Return the board status
    #ON_PROGRESS No winner for now
    #RED_WON RED player has won
    #YELLOW_WON YELLOW player has won
    #BOARD_FULL The board is full, but no winner
    return boardStatus

console.welcome()
while getBoardStatus == "ON_PROGRESS":
    if whoplay == "YELLOW":
        play(False, input("Player Yellow, enter column to play: "))
    else:
        play(True, input("Player Red, enter column to play: "))
    print(board)