# Time: O(n) -> even though two loops, it is only going through the array once
# Space: O(1) -> no extra space used -> might be considered O(n) because array returned

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        output = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            if start == end:
                output.append(str(start))
            else:
                output.append(str(start) + "->" + str(end))
            i += 1
        
        return output
