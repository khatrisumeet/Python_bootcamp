# to find sum of all students height, to find
# average of all students height
# to find total number of studnets

a = (input("height of students  "))
b = a.split(", ")
print(b)
c = len(b)
z = 0
for i in b:
    z = z+int(i)

x = z/c

print("sum of all students height is", z)
print("average of all students height", x)
print("number of students are", c)