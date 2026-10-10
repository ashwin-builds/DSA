# Time: O(n)
# Space: O(n)

# IDEA: At each level, only the right most node will be visible. So, recurse the right first then go to left. Keep a dict of 
#       the value on the right most so far for that level.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        level = 1
        level_to_value = {}
        level_to_value[level] = root.val 

        self.recursive_helper(root.right, level + 1, level_to_value)
        self.recursive_helper(root.left, level + 1, level_to_value)

        return list(level_to_value.values())

    def recursive_helper(self, root, level, level_to_value):
        if root:
            if level not in level_to_value.keys():
                level_to_value[level] = root.val
            self.recursive_helper(root.right, level + 1, level_to_value)
            self.recursive_helper(root.left, level + 1, level_to_value)