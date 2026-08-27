# Time: O(n)
# Space: O(1)

# NOTE: While the solution creates a 'results' array which would be considered O(n) space, 
#   we consider it to be linear time because its required for the problem (not extra space).

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1

        # the result list is in decreasing order, but we want non-decreasing order

        result.reverse() # time: O(n)

        return result
