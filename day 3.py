def find_duplicate(nums):
    # phase 1: meet somewhere in the cycle
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # phase 2: find the cycle entrance (duplicate)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# Tests from the sheet
print(find_duplicate([1,3,4,2,2]))      
print(find_duplicate([3,1,3,4,2]))      
print(find_duplicate([1,1]))            
print(find_duplicate([1,4,4,2,3]))      
