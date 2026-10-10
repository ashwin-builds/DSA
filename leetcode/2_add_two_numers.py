# Time: O(n)
# Space: O(n + m)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_pointer = l1
        l2_pointer = l2
        output_list = ListNode() # create empty starting node which will be deleted at end
        output_list_pointer = output_list
        
        carry_over = 0
        while l1_pointer != None and l2_pointer != None:
            current_digit_sum = l1_pointer.val + l2_pointer.val + carry_over
            new_digit, carry_over = self.calc_digit_and_rem(current_digit_sum)
            output_list_pointer.next = ListNode(new_digit)

            output_list_pointer = output_list_pointer.next
            l1_pointer = l1_pointer.next
            l2_pointer = l2_pointer.next

        while l1_pointer != None:
            current_digit_sum = l1_pointer.val + carry_over
            new_digit, carry_over = self.calc_digit_and_rem(current_digit_sum)
            output_list_pointer.next = ListNode(new_digit)
            output_list_pointer = output_list_pointer.next
            l1_pointer = l1_pointer.next

        while l2_pointer != None:
            current_digit_sum = l2_pointer.val + carry_over
            new_digit, carry_over = self.calc_digit_and_rem(current_digit_sum)
            output_list_pointer.next = ListNode(new_digit)
            output_list_pointer = output_list_pointer.next
            l2_pointer = l2_pointer.next

        if carry_over != 0:
            output_list_pointer.next = ListNode(carry_over)

        output_list = output_list.next # remove the initial dummy ListNode
        return output_list

    def calc_digit_and_rem(self, current_sum):
        new_digit = current_sum % 10
        carry_over = current_sum // 10
        return new_digit, carry_over
