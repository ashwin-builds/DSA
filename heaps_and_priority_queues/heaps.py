# MinHeap / Priority Queue

# Building the Heap / heapify - time: O(n); space: O(1)

import heapq
tree = [-4, 3, 1, 0 , 2, 5, 10, 8, 12, 9] # a regular binary tree, not a heap
print(f"Binary Tree: {tree}")

heapq.heapify(tree) # converts to a heap

print(f"MinHeap: {tree}")

# Heap Push - Insert node
# Time: O(logn)

heapq.heappush(tree, 4)

print()
print(f"MinHeap: {tree}")

# Heap Pop - Remove min
# Time: O(logn)

minn = heapq.heappop(tree)
print()
print(f"Min: {minn}")
print(f"MinHeap: {tree}")

# Heap Sort 
# Time: O(nlogn) >> among the best of sorting algos
# Space: O(n) >> O(1) is possible via swapping but a bit complex

def heap_sort(arr):
    heapq.heapify(arr) # O(logn)
    n = len(arr)
    new_arr = [0] * n # O(n) space

    for i in range(n): # O(n)
        minn = heapq.heappop(arr) # O(logn)
        new_arr[i] = minn

    return new_arr

# O(n) * O(logn) = O(nlogn) time complexity

unsorted_arr = [1, 7, 9 ,4 , 5, 3, 2, 6, 0]
print()
print(f'Unsorted Arr: {unsorted_arr}')
print(f'Sorted Arr: {heap_sort(unsorted_arr)}')

# Heap Push Pop (Push and Pop at the same time) - O(2logn) = O(logn)
print()
print(f'MinHeap: {tree}')
heapq.heappushpop(tree, 99)
print(f'MinHeap: {tree}')

# Peak at min 
# Time - O(1)
print()
print(f"Peak at Min: {tree[0]}")


# For a max heap, we need to negate the values and use heapq because heapq only works with minheaps

tree2 = [-4, 3, 1, 0 , 2, 5, 10, 8, 12, 9] # a regular binary tree, not a heap

print()
print(f"Binary Tree: {tree2}")
n = len(tree2)

# negate all nodes
for i in range(n):
    tree2[i] = -1 * tree2[i]

heapq.heapify(tree2)
print(f"Negative Min Heap (MaxHeap): {tree2}")

largest = -1 * heapq.heappop(tree2)
print(f"Largest value: {largest}")

# Now to push into the maxheap, we push the negative of the value
heapq.heappush(tree2, -7) # insert +7 into the max heap
print(f"Negative Min Heap (MaxHeap): {tree2}")


# To build a heap from scratch without heapify - O(nlogn)
print()

tree3 = [-5, 4, 2, 1, 7, 0, 3]
n = len(tree3)
heap = []
for i in range(n): # O(n)
    heapq.heappush(heap, tree3[i]) # O(logn)
    print(heap)

# O(n) * O(logn) = O(nlogn)

# Check the size of the heap (number of total nodes) - O(1)
print(f"HeapSize: {len(heap)}")

# len() in python is almost always constant time
