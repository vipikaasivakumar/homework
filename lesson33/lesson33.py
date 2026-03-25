# Lesson 33
#For testing the code:
from random import seed
from random import randrange

seed(1)# helps generate same amount of random numbers
data = [randrange(1,100) for i in range(randrange(10,30))] #list comprehension
print(f"Random datasetL {data}")

def mean(aList):
    return sum(aList) / len(aList)

print(f"Mean of dataset:{mean(data)} ")

def median(aList):
    sorted_aList = sorted(aList) # rmb sorted() MAKES NEW list, aList.sort() --> mutates existing list
    middle  = len(aList)//2
    
    if len(aList)%2 == 0: #even number of data points
        left = sorted_aList[middle-1] #Ex: [1,2,3,4] left is 4/2 so middle is 2, 2-1 at index 1 value 2
        right = sorted_aList[middle] #Ex: right is middle index 2 so value 3
        return (left+right)/2
    else:
        return sorted_aList[middle]

print(f"Median of dataset: {median(data)}")

