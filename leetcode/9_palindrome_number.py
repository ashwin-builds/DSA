# Time: O(n)
# Space: O(1)
# IDEA: reverse the number using arithmetic and compare

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # simple negative number case 
        if x < 0:
            return False
        
        rev_num = 0
        temp = x 

        while temp > 0:
            rev_num = rev_num * 10 + (temp % 10)
            temp = temp // 10

        return x == rev_num
