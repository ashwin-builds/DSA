class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        current_max_water = 0
        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            current_max_water = max(water, current_max_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return current_max_water