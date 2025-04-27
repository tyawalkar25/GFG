class Solution:
    def twoSum(self, prices):
        n = len(prices)
        buy_price = prices[0]
        sell_price = 0
        for i in range (1,n):
            buy_price = min(buy_price,prices[i])
            sell_price = max(sell_price,prices[i]-buy_price)
        return sell_price



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.twoSum([7, 6, 4, 3, 1])
   print(ans)