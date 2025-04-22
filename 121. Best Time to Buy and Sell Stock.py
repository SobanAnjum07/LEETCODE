class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy, sell = 0, 1

        max_profit = 0

        while sell < len(prices):

            current_profit = prices[sell] - prices[buy]

            if prices[buy] < prices[sell]:

                max_profit = max(current_profit, max_profit)

            else:
                buy = sell

            sell += 1

        return max_profit


        