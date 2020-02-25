class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            # 可以達成 buy於 sell之前
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
                
        
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(prices = [7,1,5,3,6,4]))
        