# Lesson 10
phone = ''
digits = True
while digits:
    phone  = input("Enter the last 4 digits of your phone number: ")
    if len(phone) == 4:
        digits = False

if phone[0] == '8' or phone[0] == '9':
    if phone[1] == phone[2]:
        if phone[3] == '8' or phone[3] == '9': #if you are printing a statement, then else is necessary
            print("This phone number is a telemarketer.")
        else: 
            print("This phone number is not a telemarketer.")
    else:
        print("This phone number is not a telemarketer.")
else: 
    print("This phone number is not a telemarketer.")