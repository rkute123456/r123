def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    # Traverse from right to left
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Reverse to maintain original order
    leaders.reverse()
    return leaders


# Example Test Cases
print(findLeaders([16, 17, 4, 3, 5, 2]))   
print(findLeaders([1, 2, 3, 4, 0]))        
print(findLeaders([7, 10, 4, 10, 6, 5, 2]))
print(findLeaders([5]))                    
print(findLeaders([100, 50, 20, 10]))     
print(findLeaders([1, 2, 3, 1000000]))     
