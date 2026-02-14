# Lesson 7
from random import randrange
difficulty = int(input("Enter DC: "))

playerRoll = randrange (1,21) #randrange doesn't include second value
print (f"The player has rolled {playerRoll} on their D20.")

if playerRoll >= difficulty:
    print(f"The player was successfull as {playerRoll} is >= {difficulty}")
else:
    print(f"The player was unsuccessfull as {playerRoll} is < {difficulty}")
    