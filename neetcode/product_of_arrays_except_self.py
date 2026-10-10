class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = []
        current_prod = 1
        for num in nums:
            l_prod.append(current_prod)
            current_prod *= num
        
        r_prod = []
        current_prod = 1
        for num in nums[::-1]:
            r_prod.append(current_prod)
            current_prod *= num
        r_prod = r_prod[::-1]

        return [i * j for i, j in zip(l_prod, r_prod)]
