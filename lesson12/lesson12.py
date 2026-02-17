# Lesson 12
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if angle1+angle2+angle3 != 180:
    print("Inputted angles do not create a triangle")
else:
    if angle1 == angle2 == angle3:
        print("Equilateral triangle")
    elif angle1 != angle2 and angle1 != angle3 and angle2 != angle3:
        print("Scalene triangle")
    else:
        print("Isoceles triangle")