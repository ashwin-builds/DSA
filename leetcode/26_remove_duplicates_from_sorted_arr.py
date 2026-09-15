# Time: O(n)
# Space: O(1) -> in place

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        viewing_index = 0 # used to keep track of the current list element being observed
        insert_index = 0 # used to keep track of where to insert the viewing element into the list
        
        while viewing_index < len(nums):
            while viewing_index < len(nums) - 1 and nums[viewing_index] == nums[viewing_index + 1]:
                viewing_index += 1
            nums[insert_index] = nums[viewing_index]
            insert_index += 1
            viewing_index += 1

        return insert_index
