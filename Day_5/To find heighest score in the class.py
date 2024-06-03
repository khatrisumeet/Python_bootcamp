z = input("score records: ")
y = z.split(", ")
print(y)
m = y[0]
for i in y:
    if i > m:
        m = i
print(m, "is the heighest score in class")