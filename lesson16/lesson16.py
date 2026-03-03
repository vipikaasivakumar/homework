# Lesson 16
# Example of range: range(x) --> [0, x) ... range(5) --> 0,1,2,3,4
# range (a,b) --> [a, b) ... range(5,10) --> 5,6,7,8,9
# range (a,b, step) --> but it will have "step" based interval
    # range (10, 0, -1) --> 10,9,8,7,6,5,4,3,2,1
    # range (1, 10, 2) --> 1, 3, 5, 7, 9
# range() is a generator function that creates iterable integers in a given parameter

for num in range (1,51): #for loops are finite loops and in other languages can be called "for each"; commonly used to look through values in iterable object
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
