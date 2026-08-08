# Selection Sort
# Time: O(n^2)
# Space: O(n)

def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

selection_sort(arr)

print(f"Sorted Array: {arr}")
