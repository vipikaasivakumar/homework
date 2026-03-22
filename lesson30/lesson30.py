# Lesson 30
num = int(input("Enter an integer greater than zero :"))
def pattern (num):
    line = " "
    for i in range(num):
        if i%2 == 0:
            line += "1"
        else:
            line += "0"
    
    return line

def output(num):
    for i in range(1, num+1):
        print(pattern(i))

ans = output(num)
print(ans)