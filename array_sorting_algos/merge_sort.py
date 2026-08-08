# Merge Sort -> recursive
# Time: O(nlogn) 
# Space: O(n)

def merge_sort(arr):
    n = len(arr)

    # Base Case 
    if n == 1 or n == 0:
        return arr 

    # Recursive Case 
    m = n // 2 # floor division
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])

    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
    
    return sorted_arr


arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

arr = merge_sort(arr)

print(f"Sorted Array: {arr}")
