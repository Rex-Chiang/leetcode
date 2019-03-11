# 設定左右邊界，並向中心前進
# 由於容量由最短線決定
# 直接計算邊界到最底端即可
# 因此都由左右邊界中較短一邊向中心前進
# 否則算出來的容積僅為前一步再少一段的容積

class Solution:
    def maxArea(self, height):
        # 若只有兩個元素，回傳最低元素
        if len(height) == 2:
            return min(height)
        
        ans = 0
        left = 0
        right = len(height)-1

        while right-left >= 1:
            
            n = right-left
            
            if min(height[left], height[right]) * n > ans:
                ans = min(height[left], height[right]) * n
            
            # 選擇較短一邊向中心前進
            if height[left] > height[right]:
                right -= 1
                
            else:
                left += 1

        return ans
    
    
if __name__=="__main__":

    s = Solution()    
    print(s.maxArea(height = [2,3,4,5,18,17,6]))