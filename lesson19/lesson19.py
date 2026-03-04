# Lesson 19 for the hundredth time T-T
num = int(input("Enter a number: "))
isPrime = True

for i in range(2, num): #start from 2 bc 1 is neither
    if num%i == 0:
        isPrime = False  #if divider (i) is factor it is not prime as i is not the number (num is exclusive in range)
        break
if isPrime:
    print(f"{num} is prime.")
else:
    print(f"{num} is composite.")
