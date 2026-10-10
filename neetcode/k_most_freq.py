# IMPORTANT IDEA: Use the index of the array to represent the 
#                 count of the value since the count is at 
#                 least 0 and at most the length of the array.
# Time: O(n)
# Space: O(n) -> for the dict (the array is constant space)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter[num] += 1
            else:
                counter[num] = 1
        
        counter_list = [0] * (len(nums) + 1)

        for num in counter.keys():
            count = counter[num]
            if counter_list[count] == 0:
                counter_list[count] = [num]
            else:
                counter_list[count].append(num)
        
        ret = []
        for i in range(len(nums), -1, -1):
            if k == 0:
                break 
            elif counter_list[i] != 0:
                    ret.extend(counter_list[i])
                    k -= len(counter_list[i])
        
        return ret
