# Lesson 20

# Answer with while loop

# num = 10000
# counter = 0
# divisor = 1
# sum = 0
# sumOfperfects = 0
# while counter < num:
#     while divisor < counter:
#         if counter % divisor == 0:
#             sum += divisor
#         divisor += 1
#     if sum==counter:
#         sumOfperfects+=sum
#     counter += 1
#     divisor = 1
#     sum = 0

# print(sumOfperfects)

#Answer with Nested For Loops
totalSum = 0
for i in range(1,10000):
    factorsSum = 0
    for factor in range(1,i):
        if i%factor == 0:
            factorsSum += factor
    if factorsSum == i: #this means perfect number
        totalSum += i

print(f"The total sum of all perfect numbers under 10,000 is {totalSum}")