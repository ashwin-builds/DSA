# Sliding Window (variable length)

# Time: O(n)
# Space: O(n) -> set to keep track of seen letters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # sliding window approach
        l = 0
        longest = 0
        n = len(s)
        sett = set() # keeps track of seen chars
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            w = (r - l) + 1 # length of current substring without repeats
            longest = max(w, longest)

        return longest
