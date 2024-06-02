import  random
a = ["ram", "piya", "sumeet", "om"]

n = random.randint(1,4)
if n == 1:
    c = (a[0])
elif n ==2:
    c = (a[1])
elif n ==3:
    c = (a[2])
else:
    c = (a[3])

print(c, "is going to pay today's bill")


