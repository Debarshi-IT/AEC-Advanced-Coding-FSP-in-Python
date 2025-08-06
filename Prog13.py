'''
Fill up a marix with dimension nxn (where is a user given integer number) with numbers ranging from 1 to n^2.
Use these numbers once in a clockwise spiral fashion starting from top-left corner.

n = 5 (user given integer)

  |  0   1   2   3   4
------------------------
0 |  1   2   3   4   5
1 |  16  17  18  19  6
2 |  15  24  25  20  7
3 |  14  23  22  21  8
4 |  13  12  11  10  9
------------------------
'''

while True:
    n = int(input("Please enter the matrix dimension (odd number): "))
    if n % 2 == 1:
        break
total_elements = n * n
print(f"So the total number of elements for matrix with dimension {n}x{n} is {total_elements}...")
matrix = [[0 for _ in range(n)] for _ in range(n)]
print("Filling up the matrix in spiral order...")
top = 0
bottom = n - 1
left = 0
right = n - 1
value = 1
while value <= total_elements:
    for col in range(left, right + 1):
        matrix[top][col] = value
        value += 1
    top += 1
    for row in range(top, bottom + 1):
        matrix[row][right] = value
        value += 1
    right -= 1
    for col in range(right, left - 1, -1):
        matrix[bottom][col] = value
        value += 1
    bottom -= 1
    for row in range(bottom, top - 1, -1):
        matrix[row][left] = value
        value += 1
    left += 1
print("Printing the matrix:")
for row in range(n):
    for col in range(n):
        print("%4d" % matrix[row][col], end="")
    print()
print("End of the program...")
