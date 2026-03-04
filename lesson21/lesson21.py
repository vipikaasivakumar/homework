# Lesson 21
num = int(input("Enter a number: "))
mostFactors = 0
resultNum = 0 #used to hold num
for i in range(1, num+1):
    factors = 0 # this needs to be reset everytime to see which number has the most factors
    for divider in range(1, i+1):
        if i%divider == 0:
            factors +=1
    if factors > mostFactors:
        mostFactors = factors #update to make mostFactors hold number of factors that is the most
        resultNum = i #update to hold number with most factors
    
print(f"{resultNum} has the most factors, with {mostFactors}.")
# how to output tie, i was thinking like factors == mostFactors to print both but how would i check beyond?
        
#tie gets kinda complicated T-T
#aList []
# maxcount = ---
# if newCount == maxCount:
#     aList.append(num)
# if newCount > maxCount:
#     aList = [num]