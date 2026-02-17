# Lesson 11
point = input() # in format "10 -11"
point = point.split(' ') #.split() is from string object class and the space is the argument; "10 -11" --> ["10", "-11"]

""" longer way to convert list with numeric strings to int
fixedPoint = []
for value in point:
    fixedPoint.append(int(value)) #append = add 
"""
point = list(map(int, point)) #map creates iterable object; point is ["10", "-11"] --> turns into iterable (10, -11) --> list [10, -11]
print(point)

x, y = point
print(f"x is {x}.")
print(f"y is {y}.")

if x > 0:
    #pass # placeholder in python; useful for setting up if else and loops
    if y > 0:
        print(f"The point of ({x}, {y}) is in Quadrant 1.")
    else: 
        print(f"The point of ({x}, {y}) is in Quadrant 4.")
else: # x is negative
    if y > 0:
        print(f"The point of ({x}, {y}) is in Quadrant 2.") 
    else: 
        print(f"The point of ({x}, {y}) is in Quadrant 3.")


