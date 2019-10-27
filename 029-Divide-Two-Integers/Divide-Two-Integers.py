class Solution:
    def divide(self, dividend, divisor):
        # 先計算quo正負
        neg = (dividend<0) != (divisor<0)
        
        quo = 0
        Q = 1
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        
        while left >= divisor:
            # 以倍數計算加速
            left -= div
            quo += Q
            Q += Q
            div += div
            # 若超過則重置
            if left < div:
                div = divisor
                Q = 1
            
        if neg:
            return max(-quo, -2147483648)
        else:
            return min(quo, 2147483647)
            
if __name__ == "__main__":
    s = Solution()
    print(s.divide(dividend = 10, divisor = 3))
    