# Lesson 28

#Answer 1: returns boolean and uses slicing
def isPalindrome(word):
#ex: | H | e | l | l | o | ! | H | e | l | l | o | !
#   -6  -5  -4  -3  -2  -1   0   1   2   3   4   5
    return word == word[:: -1]

#Answer 2: Find midway and check if other end is same
def is_palindrome(word):
    if not word: #when it is an empty string
        return True
    elif len(word) < 4: #for words that are 1,2,3 characters, first and last character same = palindrome
        return word[0] == word[-1]
    else:
        midpoint = len(word) // 2 # if its odd ignore middle char
        for i in range(0, midpoint):
            left = word[i]
            right = word[-1*i -1] #ex if i = 0, it is -1
            if left != right:
                return False
        return True

print(isPalindrome(input()), is_palindrome(input()))
print(isPalindrome(input()), is_palindrome(input()))