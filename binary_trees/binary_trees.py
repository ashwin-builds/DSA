# Binary Trees and Binary Search Trees

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value 
        self.left = left 
        self.right = right

    def __str__(self):
        return str(self.value)

# Sample Tree:
#        1
#       / \
#      2   3
#     /\  /
#    4 5 10

root = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

root.left = B
root.right = C
B.left = D
B.right = E
C.left = F

print(root)

# DFS: Recursive Pre-Order Traversal - Time: O(n), Space: O(n)
def pre_order(curr):
    if not curr:
        return

    print(curr)
    pre_order(curr.left)
    pre_order(curr.right)

print()
print("Pre-order DFS:")
pre_order(root)

# DFS: Recursive In-Order Traversal - Time: O(n), Space: O(n)
def in_order(curr):
    if not curr:
        return

    in_order(curr.left)
    print(curr)
    in_order(curr.right)

print()
print("In-order DFS:")
in_order(root)

# Level-Order BFS - Time:O(n), Space: O(n)
from collections import deque
def level_order(curr):
    queue = deque()
    queue.append(curr)

    while queue: # while the queue is not empty
        curr = queue.popleft()
        print(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

print()
print("Level-Order Traversal (BFS): ")
level_order(root)

# DFS Value lookup (Contains) - Time: O(n), Space - O(n)
def search(curr, target):
    if not curr:
        return False

    if curr.value == target:
        return True 


    return search(curr.left, target) or search(curr.right, target)

print()
print(f'Tree contains 11: {search(root, 11)}')

# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

root2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

root2.left, root2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print()
print(root2)

print()
print("In order BST: ")
in_order(root2) # same function works for binary trees and BSTs

# DFS Search BST - Time: O(logn), Space: O(logn)
def search_bst(curr, target):
    if not curr:
        return False 

    if curr.value == target:
        return True

    # BST property usage:
    if target < curr.value:
        return search_bst(curr.left, target)
    else:
        return search_bst(curr.right, target)

print()
print(f"Does BST contain -1: {search_bst(root2, -1)}")
