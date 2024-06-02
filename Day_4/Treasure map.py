line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]
print("Hiding your treasure! x marks the spot")
position = input("give any position like a1: ") #where do you want to put the treasure?
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "x"

print(f"{line1}\n{line2}\n{line3}")
# the basis of your input value spot the treasure in the matrix
# such as a1, c3, b2