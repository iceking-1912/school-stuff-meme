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

mat1 = matrix_maker("Mat1")
mat2 = matrix_maker("Mat2")
# mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

def is_upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j and matrix[i][j] != 0:
                return False
    return True

def transpose(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

def sum_diagonal_elements(matrix):
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square")
    else:
        return sum(matrix[i][i] for i in range(len(matrix)))

def find_saddle_point(matrix):
    min_row = []
    for row in matrix:
        min_row.append(min(row))
    max_col = []
    for col in range(len(matrix[0])):
        max_val = max([row[col] for row in matrix])
        max_col.append(max_val)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
                return (i, j)
    return None

def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices are not the same size")
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[i])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)
        return result

def subtract_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices are not the same size")
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[i])):
                row.append(mat1[i][j] - mat2[i][j])
            result.append(row)
        return result

def multiply_matrices(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("Matrices are not compatible for multiplication")
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2[0])):
                sum = 0
                for k in range(len(mat2)):
                    sum += mat1[i][k] * mat2[k][j]
                row.append(sum)
            result.append(row)
        return result

print("Matrix 1 is:")
for row in mat1:
    print(row)
print("Matrix 2 is:")
for row in mat2:
    print(row)

# A)
print("Is Matrix 1 upper triangular?", is_upper_triangular(mat1))

# B)
transposed_mat1 = transpose(mat1)
print("Transpose of Mat1 is:")
for row in transposed_mat1:
    print(row)
    
# C)
print("Sum of diagonal elements of Mat1:", sum_diagonal_elements(mat1))

# D)
print("Addition of Mat1 and Mat2 is:")
result = add_matrices(mat1, mat2)
for row in result:
    print(row)

print("Subtraction of Mat1 and Mat2 is:")

result = subtract_matrices(mat1, mat2)
for row in result:
    print(row)


print("Multiplication of Mat1 and Mat2 is:")

result = multiply_matrices(mat1, mat2)
for row in result:
    print(row)

# E)
saddle_point_mat1 = find_saddle_point(mat1)
if saddle_point_mat1:
    print("Saddle point of Mat1 is at position", saddle_point_mat1)
else:
    print("No saddle point found in Mat1")
    
# Output:
# Matrix 1 is:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# Matrix 2 is:
# [9, 8, 7]
# [6, 5, 4]
# [3, 2, 1]
# Is Matrix 1 upper triangular? False
# Transpose of Mat1 is:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
# Sum of diagonal elements of Mat1: 15
# Addition of Mat1 and Mat2 is:
# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]
# Subtraction of Mat1 and Mat2 is:
# [-8, -6, -4]
# [-2, 0, 2]
# [4, 6, 8]
# Multiplication of Mat1 and Mat2 is:
# [30, 24, 18]
# [84, 69, 54]
# [138, 114, 90]
# Saddle point of Mat1 is at position (2, 0)