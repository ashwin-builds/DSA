# Time: O(n * m) -> n is len(list1), m is len(list2)
# Space: O(1) -> linked list questions are almost always O(1) space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 != None and list2 == None:
            return list1
        elif list2 != None and list1 == None:
            return list2
        elif list1 == None and list2 == None:
            return None

        list1_temp = list1
        list2_temp = list2
        
        if list1.val <= list2.val:
            sorted_head = list1_temp 
            list1_temp = list1_temp.next
        else:
            sorted_head = list2_temp
            list2_temp = list2_temp.next

        curr = sorted_head
        while list1_temp and list2_temp:
            if list1_temp.val <= list2_temp.val:
                curr.next = list1_temp 
                list1_temp = list1_temp.next
            else:
                curr.next = list2_temp 
                list2_temp = list2_temp.next
            curr = curr.next

        if list1_temp != None:
            curr.next = list1_temp
        else:
            curr.next = list2_temp

        return sorted_head
