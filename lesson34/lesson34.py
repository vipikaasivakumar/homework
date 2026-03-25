# Lesson 34
from random import randrange

#Comma Separated Values
def csvTolist(word):
    csv = word.split(",")
    aList = []
    
    for i in csv:
        aList.append(int(i))
    
    return aList
    #simpler way using list comprehension: return[int(i) for i in word.split(",")]

print(csvTolist("1,2,3,4,5"))

#Return a list of random frequency of integers
def randList (start, end, frequency):
    if start < end and frequency > 0:
        aList = []
        for i in range(frequency):
            newValue = randrange(start, end+1)
            aList.append(newValue)
    else:
        return []
    #using list comprehension: return [randrange(start, end+1) for i in range(frequency)]
    return aList

print (randList(1,1000,30))