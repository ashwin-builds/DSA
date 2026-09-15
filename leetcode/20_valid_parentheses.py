# Time: O(n)
# Space: O(n) -> stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        bracket_pairs = {')' : '(', ']' : '[', '}' : '{'}

        for i in range(len(s)):
            current_bracket = s[i]

            if current_bracket in bracket_pairs.values():    # open bracket logic
                stack.append(current_bracket)
            else:                                   # close bracket logic
                if not stack or bracket_pairs[current_bracket] != stack[-1]:
                    return False
                stack.pop()

        return not stack # return true if all brackets are closed => stack is empty
