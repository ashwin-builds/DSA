# Quick Sort -> recursive
# Time: O(nlogn) -> avg time; worst case would be O(n^2) if bad pivot everytime
# Space: O(n)

def quick_sort(arr):
    n = len(arr)

    # Base Case:
    if n <= 1:
        return arr

    # Recursive Case:
    p = arr[-1] # pivot arbitrarily chosen as last element
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

print(f"Unsorted Array: {arr}")

arr = quick_sort(arr)

print(f"Sorted Array: {arr}")
