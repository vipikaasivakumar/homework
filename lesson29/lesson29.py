# Lesson 29
def consonantCount(word, vowel = False):
    counter = 0 #counts consonant and increase each time you find one
    for char in word:
        char = char.lower()
        if char.isalpha() and char not in {"a","e","i","o","u"}:
            counter += 1

    #Extension, above is enough to just find consonants
    if not vowel:
        return counter
    else:
        counter = 0
        for char in word:
            char = char.lower()
            if char.isalpha() and char in {"a","e","i","o","u"}:
                counter += 1
        return counter

print(f"The count is {consonantCount("hello, world!", True)}")