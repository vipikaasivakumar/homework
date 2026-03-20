# Lesson 26

#Creation of function for example problem: Find number of factors for each number from 1 to N
def isDivisible (num1, num2):
    #checks if num1 is divisible by num2 and returns boolean
    return num1%num2 == 0
    
def factorCount (num):
    #Use of triple quotations to explain in longer formats
    '''function determines factors of argument
    Arg: num - an int neded to find numbers of its factors
    Returns: an int which the total amount of factors
    '''
    counter = 0
    for divider in range(1, num+1):
        # if num % divider == 0:
        if isDivisible(num, divider):
            counter+=1
    return counter


upLimit = int(input("Enter N: "))

for num in range(1, upLimit+1):
    factorSize = factorCount(num) #use of function
    print(f"{num} has {factorSize} factors.")


