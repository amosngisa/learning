# arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [14, 21, 87, 14, 50]

# i = 0

# # STEP 1
# # if arr[i] > arr[i+1]:
# #     arr[i], arr[i+1] = arr[i+1], arr[i]
# #     i += 1
    
# #     # print(arr)

# for i in range(len(arr)):
#     # repeats the process
#     for j in range(0,len(arr)-i-1):
#         # it compares each element with the next
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
            
#     print(arr)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # repeats the process
        for j in range(0,n-i-1):
            # it compares each element with the next
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        return(arr)
    


