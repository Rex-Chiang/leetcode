class Solution:
    # 插入排序法
    # 一般排序法皆須遍歷2次
    def sortColors(self, nums):
        for i in range(1, len(nums)):
            tmp = nums[i]
            j = i-1
            while (j >= 0) and (tmp < nums[j]):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = tmp
            
            
    # 利用雙指標達成只遍歷一次
    def sortColors2(self, nums):
        i = 0 # white
        l = 0 # red
        r = len(nums)-1 # blue
        
        while i <= r:
            # nums[i]為red
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            # nums[i]為white
            elif nums[i] == 1:
                i += 1
            # nums[i]為blue
            # 交換後nums[i]可能為0因此i不+1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1