# Lesson 27
def stringClean (word):
    result  = ""
    for char in word:
        #since strings are IMMutable can't mutate characters you don't want that's why we use an empty string and add
        if char.isalpha():
            result += char.lower()
    return result

value = stringClean(input())
print(f"Value is {value}")