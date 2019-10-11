class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    # 深度優先搜尋演算法
    def dfs(self, nums, target, index, path, res):
        # 當 target 為 0 便無繼續必要
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            #　當 target 小於 0 便無繼續必要
            if nums[i] > target:
                break
            #　串列相加會賦新記憶體地址
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
            
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum(candidates = [2,3,5], target = 8))
    