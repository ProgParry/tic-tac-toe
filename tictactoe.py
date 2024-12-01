#!/usr/bin/python3

import os, re, random

delimiter = "---------"

os.system('clear')
name1 = input("Player 1 name: ")
name2 = input("Player 2 name: ")
print(f"\nWelcome {name1} and {name2}!")
os.system('sleep 3')
wins1 = 0
wins2 = 0

def howto():
    print("Here is the layout: \n")
    print(" 1 | 2 | 3 ")
    print(" --------- ")
    print(" 4 | 5 | 6 ")
    print(" --------- ")
    print(" 7 | 8 | 9 \n")
    input("Press enter when you are ready to play... ")

def game():
    global wins1,wins2
    p1count = 0
    p2count = 0
    rows = [
    [" ", " | ", " ", " | ", " "],
    [" ", " | ", " ", " | ", " "],
    [" ", " | ", " ", " | ", " "]
    ]
    pick = ["X","O"]
    p1XO = random.choice(pick)
    if p1XO == "X":
        p2XO = "O"
        p1goesfirst = True
    else:
        p2XO = "X"
        p1goesfirst = False
    winner = False
    while True:
        os.system('clear')
        print(f"{name1}: {p1XO} Wins: {wins1}")
        print(f"{name2}: {p2XO} Wins: {wins2}\n")
        def TicTacToe():
            for count in range(len(rows)):
                print("".join(map(str, rows[count])))
                if count < 2:
                    print("".join(map(str, delimiter)))
        TicTacToe()

        while True:
            if p1goesfirst:
                choice = input(f"{name1} choose: ")
                XO = p1XO
            else:
                choice = input(f"{name2} choose: ")
                XO = p2XO
            choices = {
                    "1":[0,0],
                    "2":[0,2],
                    "3":[0,4],
                    "4":[1,0],
                    "5":[1,2],
                    "6":[1,4],
                    "7":[2,0],
                    "8":[2,2],
                    "9":[2,4] }
            if choice not in choices.keys():
                print(f"'{choice}' is not a valid choice, try again.")
                os.system('sleep 3')
            elif rows[choices[choice][0]][choices[choice][1]] != " ":
                print(f"Somebody already chose that spot!")
                os.system('sleep 3')
            else:
                break
        
        row_choice = choices[choice][0]
        column_choice = choices[choice][1]
        p1goesfirst = not p1goesfirst
        rows[row_choice][column_choice] = XO

        # by row
        for x in range(3):
            p1count = 0
            p2count = 0
            for y in range(3):
                if rows[x][y * 2] == p1XO:
                    p1count += 1
                elif rows[x][y * 2] == p2XO:
                    p2count += 1
            if p1count == 3 or p2count == 3:
                winner = True
                break
        # by column
        if not winner:
            for y in range(3):
                p1count = 0
                p2count = 0
                for x in range(3):
                    if rows[x][y * 2] == p1XO:
                        p1count += 1
                    elif rows[x][y * 2] == p2XO:
                        p2count += 1
                if p1count == 3 or p2count == 3:
                    winner = True
                    break
        # by diagonal
        if not winner:
            p1count = 0
            p2count = 0
            for x in range(3):
                if rows[x][x * 2] == p1XO:
                    p1count += 1
                elif rows[x][x * 2] == p2XO:
                    p2count += 1
            if p1count == 3 or p2count == 3:
                winner = True
            else:
                p1count = 0
                p2count = 0
                for x in range(3):
                    if rows[x][4 - (x * 2)] == p1XO:
                        p1count += 1
                    elif rows[x][4 - (x * 2)] == p2XO:
                        p2count += 1
                if p1count == 3 or p2count == 3:
                    winner = True
        # tie?
        if not winner:
            blank = False
            for x in range(3):
                for y in range(3):
                    if rows[x][y * 2] == " ":
                        blank = True
                        break
                else:
                    continue
                break

        if not blank:
            print("Oh no! It's a tie!\n")
            TicTacToe()
            input("\nPress enter to continue...")
            break

        if winner:
            if p1count == 3: 
                print(f"{name1} wins!\n")
                wins1 += 1
            else:
                print(f"{name2} wins!\n")
                wins2 += 1
            TicTacToe()
            input("\npress enter to continue...")
            break

while True:
    os.system('clear')
    print(f"Player 1: {name1} Wins: {wins1}")
    print(f"Player 2: {name2} Wins: {wins2}\n")
    print("Type '[e]xit' to exit")
    print("Type '[p]lay' to play")
    print("Type '[h]ow' to see how to play\n")
    menuInput = input()
    if re.fullmatch("[eE](xit)?", menuInput):
        print("goodbye!")
        os.system('sleep 3')
        break
    elif re.fullmatch("[pP](lay)?", menuInput):
        game()
    elif re.fullmatch("[hH](ow)?", menuInput):
        howto()
    else:
        print(f"'{menuInput}' is an invalid input, please try again")
        os.system('sleep 3')