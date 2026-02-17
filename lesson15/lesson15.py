# Lesson 15

#Example of While Loop
secret = True
passcode = "hehe"

while secret:
    userInput = input ("Guess passcode: ")
    if userInput == passcode:
        print ("Correct!")
        secret = False
    else:
        print ("Incorrect")

print('\n')

#Example of For Loop
userInput = input("Search for a colour: ")
colours = ['Red', 'Yellow', 'Green', 'Purple']
found = False

for colourName in colours:
    if colourName == userInput:
        print (f"{userInput} is found!")
        found = True

if not found:
    print(f"{userInput} is not found.")
