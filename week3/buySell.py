class BuySellStock:
    #   Recursive method
    # def buySell(self, prices, run, total, i):
    #     if len(prices) == 0 or len(prices) == 1:
    #         return 0
    #     elif i > len(prices) - 1:
    #         return total
    #     else:
    #         dif = prices[i] - prices[i - 1]
    #         if run + dif > dif:
    #             return self.buySell(prices, run + dif, max(total, run + dif), i+1)
    #         else:
    #             return self.buySell(prices, dif, max(total, dif), i+1)

    #   DP Method
    def buySellDP(self, prices):
        running_total = maxSum = 0
        while len(prices) > 1:
            dif = prices[-1] - prices[-2]
            if running_total + dif > dif:
                running_total += dif
                prices = prices[:-1]
            else:
                running_total = dif
                prices = prices[:-1]

            maxSum = max(running_total, maxSum)

        return maxSum if maxSum > 0 else 0


p = [2, 1, 2, 1, 0, 1, 2]

print(BuySellStock().buySellDP(p))
