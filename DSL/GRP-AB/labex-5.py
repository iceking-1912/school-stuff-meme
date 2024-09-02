#labex-5-code
#insertion_sort
def insertion_sort(array):
    temp = []
    for i in array:
        temp.append(i)
    for i in range(1, len(temp)):
        key = temp[i]
        j = i - 1
        while j >= 0 and temp[j] > key:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = key
    return temp 
#shell_sort
def shell_sort(array):
    temp = []
    for i in array:
        temp.append(i)
    n = len(temp)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = temp[i]
            j = i - gap
            while j >= 0 and temp[j] > key:
                temp[j + gap] = temp[j]
                j -= gap
            temp[j + gap] = key
        gap //= 2
    return temp
#Menu
ar = []
f = False 
while (f == False):
    print("Menu- ")
    print("1. Add Array")
    print("2. Insertion Sort")
    print("3. Shell Sort")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4):"))
    if choice == 1:
        n = int(input("No. of Elements in Array:"))
        i = 0
        arr = []
        while i<n:
            arr.append(int(input("Enter Element:"))) 
            i+=1
        ar = arr.copy()
        print("Array:", ar)
    elif choice == 2:
        print("Insertion Sort:")
        print("Unsorted Array:", ar)
        temparr = insertion_sort(ar)
        print("Sorted Array:", temparr)
    elif choice == 3:
        print("Shell Sort:")
        print("Unsorted Array:", ar)
        temparr = shell_sort(ar)
        print("Sorted Array:", temparr)
    elif choice == 4:
        print("Exiting...")
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
# Enter Element:35
# Enter Element:26
# Enter Element:89
# Enter Element:22
# Enter Element:59
# Enter Element:12
# Enter Element:34
# Array: [35, 26, 89, 22, 59, 12, 34]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):2
# Insertion Sort:
# Unsorted Array: [35, 26, 89, 22, 59, 12, 34]
# Solted Array: [12, 22, 26, 34, 35, 59, 89]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):3
# Shell Sort:
# Unsorted Array: [35, 26, 89, 22, 59, 12, 34]
# Solted Array: [12, 22, 26, 34, 35, 59, 89]
# Menu-
# 1. Add Array
# 2. Insertion Sort
# 3. Shell Sort
# 4. Exit
# Enter your choice (1/2/3/4):4
# Exiting ...