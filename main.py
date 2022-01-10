# An environment to test out stuff and execute code!

# run.bat
# @echo off
# cls
# echo The date today is %date%
# echo The time today is %time%
# echo Author: Parthiv
# echo:
# echo Program Output:
# echo:
# python environment.py

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random
import os
player1 = ''
player2 = ''
gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display():
    print('_____________')
    print(f'| {gameboard[0]} | {gameboard[1]} | {gameboard[2]} |')
    print(f'| {gameboard[3]} | {gameboard[4]} | {gameboard[5]} |')
    print(f'| {gameboard[6]} | {gameboard[7]} | {gameboard[8]} |')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾')

player1 = input("Player 1, enter your name.")
player2 = input("Player 2, enter your name.")

turn = random.randint(1,2)
move = 'not'
for _ in range(1,10):
    if turn == 1:
        while move.isdigit() == False:
            move = input(f"{player1}, enter an index from 1-9.")
            if move.isdigit() == False:
                print("Please enter an integer from 1-9")
            elif move.isdigit() == True:
                if gameboard[int(move)-1] != ' ':
                    print("Please enter an index that does not have a character in it already.")
                    move = 'not'
        gameboard[int(move)-1] = 'O'
        turn = 2
        move = 'not'
        os.system('cls')
        display()
    elif turn == 2:
        while move.isdigit() == False:
            move = input(f"{player2}, enter an index from 1-9.")
            if move.isdigit() == False:
                print("Please enter an integer from 1-9.")
            elif move.isdigit() == True:
                if gameboard[int(move)-1] != ' ':
                    print("Please enter an index that does not have a character in it already.")
                    move = 'not'
        gameboard[int(move)-1] = 'X'
        turn = 1
        move = 'not'
        os.system('cls')
        display() 
