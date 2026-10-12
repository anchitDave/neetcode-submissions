class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 1
        while r < len(prices):
            tmp = prices[r] - prices[l]
            res = max(res, tmp)
            if prices[l] >= prices[r]:
                l = r
                r = l+1
            else:
                r += 1

        return res
        