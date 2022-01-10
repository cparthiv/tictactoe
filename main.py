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
# player names
player1 = ''
player2 = ''
gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
numstring=["1","2","3","4","5","6","7","8","9"]
# ways a player can win
combinations = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

def display():
    print('_____________')
    print(f'| {gameboard[0]} | {gameboard[1]} | {gameboard[2]} |')
    print(f'| {gameboard[3]} | {gameboard[4]} | {gameboard[5]} |')
    print(f'| {gameboard[6]} | {gameboard[7]} | {gameboard[8]} |')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾')

player1 = input("Player 1, enter your name.")
player2 = input("Player 2, enter your name.")
winner = ''
turn = random.randint(1,2)
move = '100'
for _ in numstring:
    if winner == 'O':
        print("The winner is player 1!")
    elif winner == 'X':
        print("The winner is player 2!")
    elif winner == '':
        if turn == 1:
            while move not in numstring:
                move = input(f"{player1}, enter an index from 1-9.")
                if move not in numstring:
                    print("Please enter an integer from 1-9")
                elif move in numstring:
                    if gameboard[int(move)-1] != ' ':
                        print("Please enter an index that does not have a character in it already.")
                        move = '100'
            gameboard[int(move)-1] = 'O'
            for c in combinations:
                trueness = 0
                for x in c:
                    if gameboard[x] == 'O':
                        trueness +=1
                if trueness == 3:
                    winner = 'O'
                
                    
            turn = 2
            move = '100'
            os.system('cls')
            display()
        elif turn == 2:
            while move not in numstring:
                move = input(f"{player1}, enter an index from 1-9.")
                if move not in numstring:
                    print("Please enter an integer from 1-9")
                elif move in numstring:
                    if gameboard[int(move)-1] != ' ':
                        print("Please enter an index that does not have a character in it already.")
                        move = '100'
            gameboard[int(move)-1] = 'X'
            for c in combinations:
                trueness = 0
                for x in c:
                    if gameboard[x] == 'X':
                        trueness +=1
                if trueness == 3:
                    winner = 'X'
            turn = 1
            move = '100'
            os.system('cls')
            display() 
