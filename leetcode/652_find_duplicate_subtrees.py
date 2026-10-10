# Time: O(n^2)
# Space: O(n)

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        subtrees = defaultdict(list)
        
        def dfs(node): # pre-order traversal
            if node == None:
                return "None"

            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(subtrees[s]) == 1:
                ret.append(node)

            subtrees[s].append(node)

            return s

        ret = []
        dfs(root)
        return ret
