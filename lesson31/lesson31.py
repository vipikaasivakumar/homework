# Lesson 31
def clean(word):
    # remove digits, make it lowercase, remove special characters
    result = ""
    for c in word:
        if c.isalpha():
            result += c.lower()
    return result

# 1. Sort both strings and compare equality
def anagram1(word1, word2):
    word1 = list(clean(word1))
    word2 = list(clean(word2))
    word1.sort()
    word2.sort()
    return word1 == word2

#2. 
def anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        list_word1 = sorted(word1)
        list_word2 = sorted(word2)
        print(f"{enumerate(list_word1)}")

        for i, char in enumerate(list_word1):
            if list_word2[i] != char:
                return False
        return True

result = anagram2("bored","robed")
print(result)