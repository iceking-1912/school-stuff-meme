def matrix_maker(name="Matrix"):
    print("Enter the number of rows and columns for Matrix:")
    r = int(input("Enter the number of rows:"))
    c = int(input("Enter the number of columns:"))
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            element = int(input(f'input Element({i + 1},{j + 1}):'))
            row.append(element)
        mat.append(row)
    print(f'{name} is:')
    for row in mat:
        print(row)
    return mat
# mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

mat1 = matrix_maker("Mat1")
mat2 = matrix_maker("Mat2")

print("Matrix 1 is:")
for row in mat1:
    print(row)
print("Matrix 2 is:")
for row in mat2:
    print(row)
print("Addition of Mat1 and Mat2 is:")
mat3 = []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        sum = mat1[i][j] + mat2[i][j]
        row.append(sum)
    mat3.append(row)
for row in mat3:
    print(row)

print("Substraction of Mat1 and Mat2 is:")
mat4 = []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        sum = mat1[i][j] - mat2[i][j]
        row.append(sum)
    mat4.append(row)
for row in mat4:
    print(row)

print("Multiplication of Mat1 and Mat2 is:")
if len(mat1) != len(mat2):
    print("Matrix Multiplication is not possible")
else:
    mat5 = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            msum = 0
            for k in range(len(mat2[0])):
                msum += mat1[i][k] * mat2[k][j]
            row.append(msum)
        mat5.append(row)
for row in mat5:
    print(row)

print("Division of Mat1 and Mat2 is:")
mat6 = []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        div = mat1[i][j] / mat2[i][j]
        row.append(round(div,3))
    mat6.append(row)
for row in mat6:
    print(row)
