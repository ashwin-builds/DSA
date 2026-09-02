# Time: O(2n) = O(n)
# Space: O(1)

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minn = nums[0] # constraint given that nums is non empty
        for num in nums: # O(n)
            if abs(num) < abs(minn):
                minn = num

        if minn < 0 and abs(minn) in nums: # O(n)
            return abs(minn)
        else:
            return minn


