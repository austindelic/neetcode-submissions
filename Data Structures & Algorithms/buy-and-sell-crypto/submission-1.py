class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        for _ in range(len(prices)):
            if r > len(prices) - 1:
                break
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1


        return max_profit
        