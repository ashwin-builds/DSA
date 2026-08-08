# Insertion Sort
# Time: O(n^2)
# Space: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

insertion_sort(arr)

print(f"Sorted Array: {arr}")
