# In practice (with python), we use something else for sorting.

# Tim Sort Algorithm

# Time: O(nlogn)

arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]

# In place (constant space):
arr.sort()
print(arr)

# Out of place (O(n) space)
arr = [9, 4, 5, 6, 2, 8, 1, 0, 3, 7]
sorted_arr = sorted(arr)
print(sorted_arr)

# Sorting an array of tuples >> common in "intervals" problems
intervals = [(3, -3), (2, 2), (-5, 9), (7, 1), (0, 0)]

sorted_intervals = sorted(intervals, key = lambda t: t[0]) # sorted by the first element of tuple
print(f"Intervals sorted by index 0 element: {sorted_intervals}")

sorted_intervals = sorted(intervals, key = lambda t: t[1]) # sorted by the second element of tuple
print(f"Intervals sorted by index 1 element: {sorted_intervals}")

sorted_intervals = sorted(intervals, key = lambda t: t[1] - t[0]) # sorted by interval length
print(f"Intervals sorted by length : {sorted_intervals}")
