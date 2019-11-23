class Solution:
    def __init__(self):
        global count
        self.count = 0
    # DFS遞歸出現多次重覆計算因此 Time Limit Exceeded 
    def climbStairs(self, n):
        steps = [1, 2]
        self.dfs(steps = steps, target = n, count = self.count)
        return self.count
    
    def dfs(self, steps, target, count):
        for i in steps:
            if target-i < 0:
                break
            if target-i == 0:
                self.count += 1
                return
            self.dfs(steps, target-i, self.count)
            
    def climbStairs2(self, n):
        if n == 1:
            return 1
        # -1代表該層方法數尚未更新
        result = [-1 for i in range(n)]
        # 這裡的1、2為方法數
        result[0] = 1
        result[1] = 2
        return self.dp(n-1, result)
    
    def dp(self, n, result):
        # n層的方法數 = (n-1)層的方法數 + (n-2)層的方法數
        if result[n] == -1:
            result[n] = self.dp(n-1, result) + self.dp(n-2, result)
        return result[n]
            
        
        
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(n = 3))
        