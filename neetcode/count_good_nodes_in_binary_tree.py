# Time: O(n)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + self.recursive_helper(root.left, root.val) + self.recursive_helper(root.right, root.val)
    
    def recursive_helper(self, root, max_so_far):
        if root is None:
            return 0
        if root.val >= max_so_far:
            return 1 + self.recursive_helper(root.left, root.val) + self.recursive_helper(root.right, root.val)
        else:
            return self.recursive_helper(root.left, max_so_far) + self.recursive_helper(root.right, max_so_far)
