# Time: O(n)
# Space: O(1)

# IDEA: We can use a single loop if we keep track of max profit and min price. We keep track of min
#       price because that is the point of buying (which comes first). The max profit tells us if 
#       selling at the given price is better than what we've seen before or worse (giving us an 
#       implicit maximum selling price).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price 
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
