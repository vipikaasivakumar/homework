# Lesson 23

#my try

# inputLength = int(input("Enter the number of numbers you want to input: "))
# counter = 0
# sumOfnums = 0
# while counter < inputLength:
#     num = int(input("Enter your number: "))
#     sumOfnums += num
#     counter += 1
#     avg = sumOfnums/inputLength
# print (avg)

#Another Answer
loop = True
totalSum = 0
counter = 0

while loop:
    ans = input("Enter \"Exit\" to stop input:")
    if ans.lower().capitalize() == "Exit": 
        loop = False
        break # stops while loop
    else:
        mark = int(ans)
        if 0 <= mark <= 100:
            totalSum += mark
            counter += 1
        else:
            print("Invalid input")
average = totalSum/counter
print(f"{average} is the average")



