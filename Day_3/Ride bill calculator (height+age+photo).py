# ride problem

a = int(input("what is your height: "))

if a >120:
    print("you are eligible for ride")
    b = int(input("what is your age: "))
    if b <12:
        bill = 5
    elif b > 18:
        bill = 12
    else:
        bill =7
    c = input("wants to take a photo y or n")
    if c == "yes":
        bill = bill +3
    else:
        bill
    print(bill)

else:
    print("you are too small for this ride")


