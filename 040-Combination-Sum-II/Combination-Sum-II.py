class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.dfs(nums = candidates, target = target, start = 0, path = [], result = result)
        return result
        
    def dfs(self, nums, target, start, path, result):
        for i in range(start, len(nums)):
            # start為了避免相同元素造成重複的組合
            if (i > start) and (nums[i] == nums[i-1]):
                continue
            if nums[i] > target:
                break
            if nums[i] == target:
                result.append(path+[nums[i]])
                return 
            else:
                self.dfs(nums, target-nums[i], i+1, path+[nums[i]], result)
        
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
        