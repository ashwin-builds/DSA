# Counting Sort -> powerful for leetcode
# Time: O(k + n) -> where k is the max number
# Space: O(k)

# For now, we do it with positive numbers only to simplify

def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counting_arr = [0] * (maxx + 1)

    # populate counting_arr
    for x in arr:
        counting_arr[x] += 1

    # reorder main array
    i = 0
    for c in range(maxx + 1):
        while counting_arr[c] > 0:
            arr[i] = c 
            i += 1
            counting_arr[c] -= 1

arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

counting_sort(arr)

print(f"Sorted Array: {arr}")
