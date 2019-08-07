class Solution(object):
    def threeSum(self, nums, target):
        results = []
        for i in range(len(nums)-2):
            # 設定 window 左右邊界
            l = i + 1; r = len(nums) - 1
            # 若最小值乘3大於target 或者 最大值乘3小於target則跳出迴圈
	    # key point
            if target < 3*nums[i] or target > 3*nums[len(nums) - 1]:
                break
            # nums[i] != nums[i-1] 若本位與前一位相同避免重複比對
            if i == 0 or nums[i] != nums[i-1]:
                while l < r:
                    # 利用本位配合window左右邊界來搜尋
                    s = nums[i] + nums[l] + nums[r]
                    # 已得到欲求結果，因此左右邊界各向中心移動
                    if s == target:
                        results.append([nums[i], nums[l], nums[r]])
                        # 若左邊界下一位與目前左邊界相同，由於是重複比對，左邊界右移一位
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        # 若右邊界下一位與目前右邊界相同，由於是重複比對，右邊界左移一位
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -=1
                    # 若 s 已小於 0 表示左邊界對於右邊界已經過小
                    # 代表右邊界若繼續移動 s 只會更小，因此左邊界右移一位
                    elif s < target:
                        l += 1
                    # 若 s 已大於 0 表示右邊界對於左邊界已經過大
                    # 代表左邊界若繼續移動 s 只會更大，因此右邊界左移一位
                    else:
                        r -= 1
    
        return results
    
    def fourSum(self, nums, target):
        results = []
        # 由小至大排序，讓相同元素相鄰有助於避免重複比對
        nums.sort()
        # len(nums)-3 原因為 window 最小需為4
        for i in range(len(nums)-3):
            # 若最小值乘4大於target 或者 最大值乘4小於target則跳出迴圈
	    # key point
            if target < 4*nums[i] or target > 4*nums[len(nums) - 1]:
                break
            # nums[i] != nums[i-1] 若本位與前一位相同避免重複比對
            if i == 0 or nums[i] != nums[i-1]:
                # 利用3Sum
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum(nums = [-1,2,2,-5,0,-1,4], target = 3))
    
