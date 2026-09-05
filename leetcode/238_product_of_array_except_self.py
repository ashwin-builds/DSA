# Time: O(n)
# Space: O(n) -> a more optimal O(1) solution exists

# My first idea was to multiply all the nums and then iterate through dividing by nums[i] to get 
#   the solution. There is a constraint of no division, however.

# IDEA: If we have a * b * c * d * e, then the product without c is the product of the left terms 
#       times the product of the right terms (ie: (a * b) * (d * e))).
#       So, we can iterate through the nums array twice, once forming a left product and once 
#       forming a right product. Then, we iterate one more time and multiply the left and right 
#       products to get the solution.
#       One important idea is that to the right and left of the overall product are 1s.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l_prod = 1
        r_prod = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        
        for i in range(n):
            j = -i -1 # negative indexing to iterate in reverse
            l_arr[i] = l_prod 
            r_arr[j] = r_prod 
            l_prod *= nums[i]
            r_prod *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]
