# Lesson 8
winCount = 0
for i in range(6): # iterates 0,1,2,3,4,5 (6 times)
    currentResult = input(f"Enter game {i+1} result: ")

    if currentResult == "w":
        winCount += 1

group = 0
if winCount > 4:
    group = 1
elif winCount > 2:
    group = 2
elif winCount > 0:
    group = 3

if group == 0:
    print ("The player is eliminated")
else:
    print (f"The player is placed in group {group}")