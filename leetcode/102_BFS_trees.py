# Time: O(n)
# Space: O(n)

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if root == None:
        	return []
        
        ret = []
        queue = deque()
        queue.append(root)

        while queue:
        	level = []
        	n = len(queue)
        	for _ in range(n):
        		curr_node = queue.popleft()
        		level.append(curr_node.val)

        		if curr_node.left: queue.append(curr_node.left)
        		if curr_node.right: queue.append(curr_node.right)

        	ret.append(level)

        return ret