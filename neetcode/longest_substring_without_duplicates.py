# IDEA: Sliding Window
# Time: O(n)
# Space: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 0
        seen = set()

        while r < len(s):
            current_letter = s[r]

            while current_letter in seen:
                seen.remove(s[l])
                l += 1

            seen.add(current_letter)
            r += 1

            longest = max(longest, len(seen))

        return longest