import random
#jai, raj, rohan, mann, vipul

z = input("name of all persons in your group: ")
names = z.split(", ")
l = len(names)

random_choice = random.randint(0, l-1)

person = print(f"{names[random_choice]} is going to pay bill today !")

# all the names of group are given and program will decide randomly
# person who will pay the bill



