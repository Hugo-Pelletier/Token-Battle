BOARD_ROWS = 6
BOARD_COLUMN = 7
boardStatus = "ON_PROGRESS"
    #ON_PROGRESS No winner for now
    #RED_WON RED player has won
    #YELLOW_WON YELLOW player has won
    #BOARD_FULL The board is full, but no winner
board = []
for y in range (BOARD_COLUMN):
    boardColumn = ""
    for x in range (BOARD_ROWS):
        boardColumn += "0"
    board.append(boardColumn)
print(board)

def clearBoard():
    board = []
    
def canPlay(columnIndex): #return the cell free in this column or -1 if no cell free
    for i in range (len(boardColumn)):
        if board[columnIndex][i] == "0":
            return i
    return -1

def play( isRed, columnIndex): 
    boardCol = ""
    for i in range (len(board[columnIndex])):
        if i < canPlay(columnIndex) or i == -1:
            boardCol += board[columnIndex][i]
        elif isRed and i == canPlay(columnIndex):
            boardCol += "R"
        elif not isRed and i == canPlay(columnIndex):
            boardCol += "Y"
        else:
            boardCol += "0"
    board[columnIndex] = boardCol

    #Play on given column, as a RED player or as a YELLOW player
    #@param isRed (Boolean): If true, play a RED disk, otherwise, play a YELLOW disk
    #@param columnIndex (integer): column index to play – Column index starts from 0 to 6
    #@return you are free to return whatever you want (or nothing)
    #Note: We recommend you to return the positon (column, row) of the DISK in the board, since you might use it afterward

def getBoardStatus(): #Return the board status
    return boardStatus

