class Solution:
    def permuteUnique(self, nums):
        # 將相同的數字排列一起才能進行重複項檢查
        nums.sort()
        result = []
        self.dfs(nums, [], result)
        return result
        
    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)
        
        for i in range(0, len(nums)):
            # 若不同分支的首項相同那就會有重複的情況
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            # 有 nums[:i] 排列才能有所交叉
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], result)
            
            
if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique(nums = [1,1,2]))