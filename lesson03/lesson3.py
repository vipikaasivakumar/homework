# Lesson 3
#logic is to use square root on tiles to find the optimized length
from math import sqrt, floor #import statements
tiles = int(input("Enter a positive integer: "))
length = floor(sqrt(tiles))
print(f"The largest square has a side length of {length}")