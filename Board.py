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
            return i
    return -1

def whoPlay():
    if whoPlay == "RED":
        whoPlay = "YELLOW"
    else:
        whoPlay = "RED"
    return(whoPlay)

def play( isRed, columnIndex): 
    boardCol = ""
    for i in range (len(board[columnIndex])):
        if i < canPlay(columnIndex) or i <= 0:
            boardCol += board[columnIndex][i]
        elif isRed and i == canPlay(columnIndex):
            boardCol += "R"
        elif not isRed and i == canPlay(columnIndex):
            boardCol += "Y"
        else:
            boardCol += "0"
    board[columnIndex] = boardCol

def getBoardStatus(): #Return the board status
    #ON_PROGRESS No winner for now
    #RED_WON RED player has won
    #YELLOW_WON YELLOW player has won
    #BOARD_FULL The board is full, but no winner
    return boardStatus

