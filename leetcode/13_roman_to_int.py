# Time: O(n)
# Space: O(1)

# IDEA: If the next number is bigger than the current, we subtract the current. Otherwise, add the current

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        converter = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        i = 0
        n = len(s)
        total = 0

        while i < n:
            if i < n - 1 and converter[s[i]] < converter[s[i + 1]]:
                total -= converter[s[i]]
            else:
                total += converter[s[i]]
            i += 1

        return total
