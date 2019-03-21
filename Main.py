# John Giorshev
# 2019-03-21
# A (very) quickly made program for practicing getting matrices to RREF.

import numpy as np

print("---2D Matrix Manipulation Practice---")
print("Saves a lot of paper! No input error checking; be careful what you type :P\n")

rows = int(input("# of rows: "))
columns = int(input("# of columns: "))
print(str(rows) + " " + str(columns))
matrix = np.zeros(shape=[rows, columns])
print("Enter the matrix info with elements separated by , and rows separated by ;\n"
      "e.g. for a 4x5 matrix: 2,6,1,-4,7;1,2,-4,0,6;-1,-3,-1,1,-1;1,3,0,-3,6")
content = input(">")

row_count = 0
for s in content.split(";"):
    column_count = 0
    for n in s.split(","):
        matrix[row_count][column_count] = float(n)
        column_count += 1
    row_count += 1

print("Matrix set:\n" + str(matrix) + "\n")

initial_matrix = matrix.copy()

print("Commands:")
print("swap[row #],[row #]\ne.g. swap1,3 => swaps row 1 and 3\ne.g. swap2,2 => nothing changes")
print("set[row # to set];[int amount],[row #];[int amount],[row #];...\n"
      "e.g. set2;1,2;-2,1 => row 2 is set to 1 times row 2 plus -2 times row 1\n"
      "e.g. set2;-1,2 => row 2 is multiplied by negative 1\n"
      "e.g. set1 -> row 1 is set to all zeros")
print("exit => exits the program")
print("reset => sets the matrix to its initial values")
flag = True
while flag:
    inp = input(">")
    if inp == "exit":
        flag = False
    else:
        if inp.startswith("swap"):
            inpp = inp[4:].split(",")
            r1 = int(inpp[0]) - 1  # array starts at 0 lol
            r2 = int(inpp[1]) - 1
            store = matrix[r1].copy()
            matrix[r1] = matrix[r2]
            matrix[r2] = store
        elif inp.startswith("set"):
            inpp = inp[3:].split(";")
            newrow = np.zeros(columns)
            for s in inpp[1:]:
                inppp = s.split(",")
                newrow += int(inppp[0]) * matrix[int(inppp[1]) - 1]
            matrix[int(inpp[0]) - 1] = newrow
        elif inp == "reset":
            matrix = initial_matrix.copy()
        print("Matrix:\n" + str(matrix))