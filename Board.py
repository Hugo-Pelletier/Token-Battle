BOARD_ROWS = 6
BOARD_COLUMN = 7

def clearBoard()
    #Clear the board to start a new game
    #@return nothing!
def canPlay(columnIndex)
    #@param columnIndex (integer): column index to play – Column index starts from 0 to 6
    #@return true if you can play on this column
def play( isRed, columnIndex)
    #Play on given column, as a RED player or as a YELLOW player
    #@param isRed (Boolean): If true, play a RED disk, otherwise, play a YELLOW disk
    #@param columnIndex (integer): column index to play – Column index starts from 0 to 6
    #@return you are free to return whatever you want (or nothing)
    #Note: We recommend you to return the positon (column, row) of the DISK in the board, since you might use it afterward
def getBoardStatus()
    #@return the current board status (see below)
    #ON_PROGRESS No winner for now
    #RED_WON RED player has won
    #YELLOW_WON YELLOW player has won
    #BOARD_FULL The board is full, but no winner
