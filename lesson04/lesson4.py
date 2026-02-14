# Lesson 4
from math import ceil

section1 = input("Enter section 1: ") 
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

cans = len(section1) + len(section2) + len(section3)
boxes = ceil(cans/12) # rounding up to have enough paint cans

totalCost = 14.95*boxes
leftover = 12*boxes - cans

print(f"You need {cans} cans.")
print(f"You would have {leftover} cans leftover.")
print(f"It would cost you ${totalCost}.")
