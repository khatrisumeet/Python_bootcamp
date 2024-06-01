#pizza order system and billing system
a = input("what is size of you pizza S,M,L")
b = input("do you want to add pepperoni yes or no")
c = input("do you want to add chees yes or no")

if a=="s":
    price = 15
    if b == "y":
        price = price+2

    else:
        print(price)
    if c == "y":
        price = price+1
        print(price)
    else:
        print(price)


elif a == "m":
    price = 20
    if b == "y":
        price = price+3

    else:
        print(price)
    if c == "y":
        price = price+1
        print(price)
    else:
        print(price)
else:
    price = 25
    if b == "y":
        price = price+3

    else:
        print(price)
    if c == "y":
        price = price+1
        print(price)
    else:
        print(price)



