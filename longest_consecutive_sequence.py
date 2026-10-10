# IDEA: Get a set verssion of the array for O(1) value lookup
# Time: O(n)
# Space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numsSet: # => start of new sequence
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(longest, length)

        return longest
