def quick_sort(ar):
    if len(ar) <= 1:
        return ar
    
    n = len(ar)
    pi = n-1
    p = ar[pi]
    
    arl = []
    for x in ar:
        if x < p:
                arl.append(x)
    arr = []
    for x in ar:
        if x > p:
                arr.append(x)
                
    sorted_arl = quick_sort(arl)
    sorted_arr = quick_sort(arr)
    
    return sorted_arl + [p] + sorted_arr

ar = [10, 40, 20, 90, 60, 30, 70, 50, 80]
print("UnSorted Array:")
print(ar)
print("Sorted Array:")
sorted_ar = quick_sort(ar)
print(sorted_ar)

# Output:
# UnSorted Array:
# [10, 40, 20, 90, 60, 30, 70, 50, 80]
# Sorted Array:
# [10, 20, 30, 40, 50, 60, 70, 80, 90]