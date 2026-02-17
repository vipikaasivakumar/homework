# Lesson 13
month = int(input("Enter month in numeric value: "))
date = int(input("Enter the date: "))

if month == 2 and date == 18:
    print("Today is a special day!")
else:
    if month < 2:
        print ("Before special day :(. ")
    elif month > 2:
        print ("After special day :(. ")
    else:
        if date < 18:
            print ("Before special day :(. ")
        else:
            print ("After special day :(. ")

         