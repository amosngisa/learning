import random

n = 6
# # generate random array
arr = random.sample(range(1, 100), n)

# n = len(arr)
def selection_sort(arr):
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
        
        print(arr)
    return arr
    
print("Sorted array: ", selection_sort(arr))
    
array = [29,10,14,37,13]