

def welcome():
    print("WELCOME TO DISK-BATTLE !")

def printBoard(board):
    result = ""
    for i in range (len(board)):
        for j in range (len(board[0])):
            result += board[j][i] + " "
        result += "\n"
    print(result)