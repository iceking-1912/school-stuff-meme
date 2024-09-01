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
mat1 = [ [0, 0, 3],
         [1, 0, 0],
         [0, 2, 0]]
mat2 = [ [9, 8, 7]
        ,[6, 5, 4]
        ,[3, 2, 1]]

# mat1  = matrix_maker("Mat1")
# mat2 = matrix_maker("Mat2")

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

#transpose of matrix
#
print("Transpose of Mat1 is:")
mat4 = []
for i in range(len(mat1[0])):
    row = []
    for j in range(len(mat1)):
        row.append(mat1[j][i])
    mat4.append(row)
#
for row in mat4:
    print(row)
#
# mat5 = [] 
fmat= []
for i in range(len(mat1[0])):
    row = []
    for j in range(len(mat1)):
        if (mat1[i][j] > 0):
           row.append(mat1[j][i])
        # elif (mat1[i][j] == 0):
        #     row.append(0)
        # else:
        #     pass
    fmat.append(row) 
while [] in fmat:
    print([])

