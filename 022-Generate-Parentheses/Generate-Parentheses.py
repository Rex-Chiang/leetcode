class Solution:
    def generateParenthesis(self, n):
        result = []
        
        self.dfs(tmp="", left=n, right=n, result=result)
                    
        return result

    def dfs(self, tmp, left, right, result):
        # 避免左括弧額度還有而右括弧已沒有的情況
        if right < left:
            return
        # 若左右括弧額度已沒有則增添到答案
        if left == right == 0:
            result.append(tmp)
            
        if left > 0:
            self.dfs(tmp+"(", left-1, right, result)
            
        if right > 0:
            self.dfs(tmp+")", left, right-1, result)
                
        
if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(n = 3))