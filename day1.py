def sort_0_1_2(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1; mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr

# examples
print(sort_0_1_2([0, 1, 2, 1, 0, 2, 1, 0]))  
print(sort_0_1_2([2,2,2,2]))                 
print(sort_0_1_2([0,0,0,0]))                 
print(sort_0_1_2([1,1,1,1]))                
print(sort_0_1_2([2,0,1]))                   
print(sort_0_1_2([]))                       
