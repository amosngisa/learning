arr = [12, 11, 13, 5, 6]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i-1
    
    # shift elements of the sorted portion that are greater than the key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    # insert the key in its correct position
    arr[j + 1] = key
    
    print(arr)
        
        
