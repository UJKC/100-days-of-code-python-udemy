print("There is treasure between the 9 blocks. Find it.")
row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]
map = [row1, row2, row3]
print(f"{map[0]}\n{map[1]}\n{map[2]}\n")
print("Place in between")
row = int(input("Select the row: "))
column = int(input("Select the colum of the row: "))
map[row - 1][column - 1] = "1"
print(f"{map[0]}\n{map[1]}\n{map[2]}\n")