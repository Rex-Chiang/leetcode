class Solution:
    def maxArea(self, height):
        if len(height) == 2:
            return min(height)
        
        ans = 0
        
        for i in range(0, len(height)-1):
            k = 1
            for j in range(i+1, len(height)):
                
                if min(height[i],height[j]) * k < ans:
                    pass
                
                else: 
                    ans = min(height[i],height[j]) * k

                k+=1
                
        return ans
    
    
if __name__=="__main__":

    s = Solution()    
    print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))