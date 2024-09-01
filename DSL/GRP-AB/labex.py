# labex-4-
#RCURSIVE

# ar = [1,2,3,4,5,6,7,8,9]
# i = 9

# def swap(a,b):
#     a,b=b,a
# def is_sorted(ar):
#     n = len(ar)
#     i = 0
#     s = True
#     while i<(n-1) :
#         if ar[i] < ar[i+1]:
#             pass
#         else:
#             s = False
#         i += 1

#         if (s == True):
#             return True
#         else:
#             return False

# def bs(arr,min,max,x):
#     sor = is_sorted(arr)
#     min = 0
#     max = len(arr)
#     mid = round((min + max) // 2)
#     if not sor: 
#         if (arr[mid] == x):
#             print("Element found at:",mid)
#         elif (arr[mid] > x):
#             bs(arr,min,(round(max/2)),x)
#         elif (arr[mid] < x):
#             bs(arr,(round(max/2)),max,x)
#         else:
#             print("Element Not found")
#     else:
#         for i in arr:
#             if arr[i] > arr[i+1]:
#                 swap(arr[i],arr[i+1])
#             else:
#                 pass
# print(ar)
# print("Find Element",i,":")
# bs(ar,min,max,i)
