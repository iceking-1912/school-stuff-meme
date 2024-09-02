#labex-4-code
#bubble_sort
def bubble_sort(array):
    temp = [i for i in array]  
    n = len(temp)
    for i in range(n):
        for j in range(0, n-i-1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
    return temp

#selection_sort
def selection_sort(array):
    temp = [i for i in array]  
    for i in range(len(temp)):
        min_idx = i
        for j in range(i+1, len(temp)):
            if temp[min_idx] > temp[j]:
                min_idx = j
        temp[i], temp[min_idx] = temp[min_idx], temp[i]
    return temp
#Menu
f = False
arr = []
while (f == False):
    print("Menu- ")
    print("1. Add Array")
    print("2. Selection Sort")
    print("3. Bubble Sort")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
        n = int(input("No. of Elements in Array:"))
        arr = []
        for i in range(n):
            arr.append(int(input("Enter Element:"))) 
        print("Array:", arr)
    elif choice == 2:
        print("Selection Sort:")
        print("Unsorted Array:", arr)
        sorted_array = selection_sort(arr)
        print("Sorted Array:", sorted_array)
    elif choice == 3:
        print("Bubble Sort:")
        print("Unsorted Array:", arr)
        sorted_array = bubble_sort(arr)
        print("Sorted Array:", sorted_array)
    elif choice == 4:
        print("Exit")
        f = True
    else:
        print("Invalid choice")

# Output:
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):1
# No. of Elements in Array:7
# Enter Element:16
# Enter Element:2
# Enter Element:69
# Enter Element:24
# Enter Element:36
# Enter Element:24
# Enter Element:95
# Array: [16, 2, 69, 24, 36, 24, 95]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):2
# Insertion Sort:
# Unsorted Array: [16, 2, 69, 24, 36, 24,
# Sorted Array: [2, 16, 24, 24, 36, 69, 95]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):3
# Shell Sort:
# Unsorted Array: [16, 2, 69, 24, 36, 24,
# 95ted Array: [2, 16, 24, 24, 36, 69, 95]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):4
# Exiting ...