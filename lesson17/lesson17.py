# Lesson 17
#Factorial means the ! operator in math. Ex: 5! = 5x4x3x2x1
num  = int(input("Enter a number: "))
answer = 1
for i in range(1, num+1): #this goes from 1 to num+1 (bc range doesn't count last number)
    answer*=i
print(f"Factorial of {num} is {answer}")