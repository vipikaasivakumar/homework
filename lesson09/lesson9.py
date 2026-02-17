# Lesson 9
from random import choice

player = ''
invalid = True # using truthy falsy for user input, if input is wrong it will continuously output while loop until entered correctly
while invalid:
    player = input("Enter your choice from rock, paper, or scissors: ")

    if player in('rock', 'paper', 'scissors'): # use in operator with sets in python because of its fast execution speed
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])

if player == cpu:
    print("Tied game.")
else: #executing this block means 1 winner
    if player == 'rock':
        if cpu == 'paper':
            print("CPU won the game.")
        else:
            print("Player won the game.")

    elif player == 'paper':
        if cpu == 'scissors':
            print("CPU won the game.")
        else:
            print("Player won the game.")

    else: #player chose scissors
        if cpu == 'rock':
            print("CPU won the game.")
        else:
            print("Player won the game.")



