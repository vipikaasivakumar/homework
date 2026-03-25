# Lesson 36
def factors(num):
    result = []
    for divider in range(1, num+1):
        if num % divider == 0:
            result.append(divider)
    return result

def isPrime(num):

    return len(factors(num)) == 2

#Tests
print(f"Factors of 13: {factors(13)}")
print(f"Factors of 36: {factors(36)}")
print(f"Is 13 prime? {isPrime(13)}")
print(f"Is 36 prime? {isPrime(36)}")
