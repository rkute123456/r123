import math

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < (n + m):
            # Case 1: Both in arr1
            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < n and j >= n:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

            # Case 3: Both in arr2
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        # Update gap
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)


# 🔹 Example Run
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2)
