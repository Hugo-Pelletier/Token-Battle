import Board as b


switch = True
print("WELCOME TO DISK-BATTLE !")
while b.getBoardStatus == "ON_PROGRESS":
    if b.whoplay == "YELLOW":
        b.play(False, input("Player Yellow, enter column to play: "))
    else:
        b.play(True, input("Player Red, enter column to play: "))
    print(b.board)

b.play(True, 5)
