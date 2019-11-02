class Solution:
    # DFS
    def permute1(self, nums):
        result = []
        self.dfs(nums, [], result)
        return result
        
    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)
        
        for i in range(0, len(nums)):
            # 有 nums[:i] 排列才能有所交叉
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], result)
    
    # BFS
    def permute2(self, nums):
        result = [[]]
        # 第一個 for 讀取數字
        for num in nums:
            new_result = []
            # 第二個 for 取得較小集合
            for i in range(len(result)):
                prev = result[i]
                prev.append(num)
                # 第三個 for 插入最後一數
                for j in range(0, len(prev)):
                    # 交換位置
                    prev[j], prev[-1] = prev[-1], prev[j]
                    new_result.append(prev[:])
                    # 恢復原始位置
                    prev[j], prev[-1] = prev[-1], prev[j]
            result = new_result
        return result
        
        
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.permute2(nums = [1,2,3]))
        