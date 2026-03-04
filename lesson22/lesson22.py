# Lesson 22
fib0 = 0
fib1 = 1

num = int(input("Enter the term number: "))
for i in range(2, num+1):
    fib_num = fib1+fib0
    fib0 = fib1
    fib1 = fib_num
print(f"Fibonacci's {num}th term is {fib_num}.")
