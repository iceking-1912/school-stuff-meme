#insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [5, 2, 8, 12, 1]
print("UnSorted Array:",arr)
insertion_sort(arr)
print("Sorted Array:",arr)

# Output:
# UnSorted Array: [5, 2, 8, 12, 1]
# Sorted Array: [1, 2, 5, 8, 12

