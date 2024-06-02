x = input("choose one option rock, paper scissor: ")
import random
z = ["rock", "paper", "scissor" ]
y = random.randint(1,3)
if y ==1:
    c = (z[0])
elif y==2:
    c = (z[1])
else:
    c = (z[3])

print("computer draw", c)
if x ==c:
    print("draw")
elif x == "rock" and c == "paper":
    print("You won!")
elif x == "paper" and c == "rock":
    print("You lose!")
elif x == "rock" and c == "scissor":
    print("You won!")
elif x == "scissor" and c == "rock":
    print("You lose!")
elif x == "paper" and c == "scissor":
    print("You lose!")
elif x == "scissor" and c == "paper":
    print("You won!")



