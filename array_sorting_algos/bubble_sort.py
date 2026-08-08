# Bubble Sort
# Time: O(n^2)
# Space: O(1)

def bubble_sort(arr):
    is_done = False
    while not is_done:
        is_done = True
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]: # use < for descending order
                is_done = False
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

bubble_sort(arr)

print(f"Sorted Array: {arr}")
