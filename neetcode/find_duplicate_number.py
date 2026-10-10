# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if num < 0:
                num *= -1
                
            if nums[num] > 0:
                nums[num] *= -1
            else:
                return num