# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return

        # Step 1: Find middle
        slow = head
        fast = head.next 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # Slow now points to the end of the first list and fast points to the start of the second list or None

        # Step 2: break the second list and reverse it

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head2 = prev # head of the second list

        # Step 3: join the nodes into one final list
        first, second = head, head2
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2








