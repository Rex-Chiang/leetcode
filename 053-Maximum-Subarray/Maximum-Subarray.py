class Solution:
    # Kadane's algorithm
    # Dynamic Programming
    def maxSubArray(self, nums):
        for i in range(0, len(nums)-1):
            # 若目前元素為正便繼續向後累積
            # 若目前元素為負則跳過
            # 且向後更新目前最大值(間接形成SubArray)
            if nums[i] > 0:
                nums[i+1] += nums[i]
                
        return max(nums)
            
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
    