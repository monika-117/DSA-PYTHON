class Solution(object):
    def maxProfit(self, prices):
        sellOne = 0
        holdOne = float('-inf')

        for price in prices:
            sellOne = max(sellOne, holdOne + price)
            holdOne = max(holdOne, -price)

        return sellOne