# Lesson 25
num = int(input("Enter a number: "))
numCopy = num
largest = 0
while num%2 == 0:
    num = num//2

    largest = max(largest, 2) #swaps variable value based on condition

if num != 1: #checking other primes
    factor = 3
    while num != 1:
        if num % factor == 0:
            largest  = max(largest, factor)
            num = num//factor
        else:
            factor += 2 #checking next ODD num, guaranteed prime when code executes else 

print(f"{largest} is the pargest prime factor for {numCopy}")