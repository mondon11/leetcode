class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit = j - i
                max_profit = max(profit,max_profit)
        return max_profit
    def maxProfit1(self,prices):
        min_value = float('inf') #某时刻之前的最小值
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value
        return max_profit
