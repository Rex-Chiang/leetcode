class Solution:
    def subsets(self, nums):
        result = []
        self. DFS(nums, result, path = [])
        return result
    
    def DFS(self, nums, result, path):
        result.append(path)
        
        for i in range(0, len(nums)):
            # 防止Index out of range
            if len(nums) > 1:
                self.DFS(nums[i+1:], result, path+[nums[i]])
            else:
                result.append(path+[nums[i]])
                return
        
if __name__ == "__main__":
    s = Solution()
    print(s.subsets(nums = [1,2,3]))