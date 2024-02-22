import os
import sys

def winner(value):
    if value == player1:
        print("Player 1 has won")
        exit()
    elif value == player2:
        print("player 2 has won")
        exit()

def check_gameover():
    if tictac[0][0] == tictac[0][1] and tictac[0][1] == tictac[0][2]:
         winner(tictac[0][0])
         return True
    elif tictac[1][0] == tictac[1][1] and tictac[1][1] == tictac[1][2]:
        winner(tictac[1][0])
        return True
    elif tictac[2][0] == tictac[2][1] and tictac[2][1] == tictac[2][2]:
        winner(tictac[2][0])
        return True
    elif tictac[0][0] == tictac[1][1] and tictac[1][1] == tictac[2][2]:
        return winner(tictac[0][0])
        return True
    elif tictac[0][2] == tictac[1][1] and tictac[1][1] == tictac[2][0]:
        winner(tictac[0][2])
        return True
    elif tictac[0][0] == tictac[1][0] and tictac[1][0] == tictac[2][0]:
        winner(tictac[0][0])
        return True
    elif tictac[0][1] == tictac[1][1] and tictac[1][1] == tictac[2][1]:
        winner(tictac[0][1])
        return True
    elif tictac[0][2] == tictac[1][2] and tictac[1][2] == tictac[2][2]:
        winner(tictac[0][2])
        return True

    else:
        return False

game = True

def inputplayer1():
    print("player 1")
    row = int(input("Enter the row: ")) - 1
    column = int(input("Enter the column: ")) - 1
    assign_value1(row, column)
def inputplayer2():
    print("player 2 ")
    row = int(input("Enter the row: ")) - 1
    column = int(input("Enter the column: ")) - 1
    assign_value2(row, column)


def display():
    for tic in tictac:
        for i in tic:
            print(i  + "  |", end=' ')
        print("", end="\n")
        print("--------------")


def assign_value1(row, column):
    count_row = 0
    for tic in tictac:
        if count_row == row:
            if tic[column] == " ":
                tic[column] = player1

                display()
                check_gameover()
            else:
                print("you can't reassign ")
                inputplayer1()
        count_row += 1
def assign_value2(row, column):
    count_row = 0
    for tic in tictac:
        if count_row == row:
            if tic[column] == " ":
                tic[column] = player2
                display()
                check_gameover()

            else:
                print("you can't reassign to a position that was already made")
                inputplayer2()

        count_row += 1

print("Welcome  ")
print("  |    |     |")
print("--------------")
print("  |    |     |")
print("--------------")
print("  |    |     |")

tictac = [
    [" ", " ", " "],

    [" ", " ", " "],

    [" ", " ", " "],
]

player1 = input("player 1 choose X or O ").upper()
player2 = ""
if player1 == "O":
    player2 = "X"
elif player1 == "X":
    player2 = "O"
else:
    sys.exit("you did not enter X or O")

while game:


    inputplayer1()
    inputplayer2()
    game = check_gameover()










