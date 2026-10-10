# Time: O(n)
# Space: O(n) -> recursive call stack pushed to n times

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if head is None or head.next == None:
            return head

        newHead = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return newHead