class Solution:
    def removeDuplicates(self, nums):
        cur = 0
        while cur+2 < len(nums):
            if nums[cur] == nums[cur+2]:
                nums.pop(cur)
            else:
                cur += 1
        return nums
        
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates(nums = [1,1,1,2,2,3]))
        