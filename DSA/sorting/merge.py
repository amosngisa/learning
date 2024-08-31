
arr = [38, 27, 43, 3, 9, 82]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        print(arr)
        
        # while i < len(left) and j < len(right):
        #     if left[i] < right[j]:
        #         arr[k] = left[i]
        #         i +=1
        #         # print(arr)
        #     else:
        #         arr[k] = right[j]
        #         j +=1
        #         # print("aa",arr)
        #     k +=1
        # while i < len(left):
        #     arr[k] = left[i]
        #     i += 1
        #     k += 1
        #     # print(arr)
        # while j < len(right):
        #     arr[k] = right[j]
        #     j += 1
        #     k += 1
            # print(arr)
            
        # print(arr)
        
    return arr

print(merge_sort(arr))