# Lesson 35
test = ["a", "b", "c", "c", "b", "c","a","a", "d"]
print(f"Test list: {test}")

def removeDuplicates(aList):
    newList = []
    for i in aList:
        if i not in newList:
            newList.append(i)
    return newList
    
print(f"Duplicates removed: {removeDuplicates(test)}")