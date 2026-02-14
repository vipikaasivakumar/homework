# Lesson 5
# Version 1 without .count()

# startMoney = float(input("Enter the amount of money you are starting with: ")) #float helps cast its argument to REAL number
# cookiesSold = input("Enter cookies: ")

# cookies = 0
# bigCookies = 0
# for currentCookie in cookiesSold:
#     if currentCookie == "c":
#         cookies += 1
#     elif currentCookie == "b":
#         bigCookies += 1
#     else:
#         print(f"{currentCookie} is not a valid cookie type")

# totalCookies = cookies+bigCookies
# profit = (bigCookies*1.25) + (cookies*0.25)
# endMoney = startMoney + profit

# print(f"You sold {totalCookies} cookies with a profit of ${profit}. You now have ${endMoney}.")

#Version 2 with .count()

startMoney = float(input("Enter the amount of money you are starting with: ")) #float helps cast its argument to REAL number
cookiesSold = input("Enter cookies: ")

cookies = cookiesSold.count('c')
bigCookies = cookiesSold.count('b')

totalCookies = cookies+bigCookies
profit = (bigCookies*1.25) + (cookies*0.25)
endMoney = startMoney + profit

print(f"You sold {totalCookies} cookies with a profit of ${profit}. You now have ${endMoney}.")
