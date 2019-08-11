class Solution(object):
    def nextPermutation(self, nums):
        l, r = 0, len(nums) - 1
        # 由後向前檢測後段降冪的斷點
        while (nums[r] <= nums[r-1]) and (r > 0):
            r-=1
        # 由後向前檢測，若檢測至第一位仍未有斷點，則整個nums為降冪，因此回傳nums的反向列，也就是升冪排列
        if r == 0:
            nums.reverse()
            return 
        # 紀錄後段降冪的斷點
        l = r-1
        # 找出斷點之後且大於斷點的最小值
        for i in range(len(nums)-1, l, -1):
            if nums[i] > nums[l]:
                switch = i
                break
        # 斷點與前段所找出的最小值交換位置
        nums[l], nums[switch] = nums[switch], nums[l]
        # 原先斷點後段的值進行升冪排列
        self.reverse(nums, l+1, len(nums)-1)
        return nums
    
    # 回傳的反向列
    def reverse(self,nums,left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()
    print(s.nextPermutation([6, 5, 4, 8, 7, 5, 1]))