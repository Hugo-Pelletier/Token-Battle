def welcome():
    print("WELCOME TO DISK-BATTLE !")

def printBoard(board):
    result = ""
    for i in range (len(board)-1, -1, -1):
        for j in range (len(board[0])):
            result += board[j][i] + " "
        result += "\n"
    print(result)

def yellowWon():
    print("Yellow Won !")

def redWon():
    print("Red Won !")

def boardFull():
    print("The board is full !")