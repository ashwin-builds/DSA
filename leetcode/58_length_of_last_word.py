# Time: O(n) -> although iterating from back means it is rarely this bad
# Space: O(1)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = -1
        n = len(s)
        num_spaces = 0
        while s[length] == ' ':
            num_spaces += 1
            length -= 1
        while abs(length) < n:
            if s[length - 1] == ' ':
                return abs(length) - num_spaces
            length -= 1

        return abs(length) - num_spaces
