# Queue - implemented using doubly linked list
# FIFO - first in, first out

from collections import deque # careful of the spelling

# deque means doubly ended queue so we could actually add / remove from either side
# for now we will use it as a reegular queue

queue = deque()
print(f"Queue: {queue}")

# enqueue > add elements to right - O(1)
queue.append(1)
queue.append(2)
queue.append(3)

print(f"Queue: {queue}")

# dequeue > remove elements from right - O(1)
x = queue.popleft() # use popleft because pop removes right > doubly ended queue
print(f"Removed element: {x}")
print(f"Queue: {queue}")

# Peek at left side - O(1)
print(f"First element: {queue[0]}")

# Peek at right side - O(1)
print(f"Last element: {queue[-1]}")
