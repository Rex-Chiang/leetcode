class Solution:
    def threeSum(self, nums):
        ans = []
        # 由小至大排序，讓相同元素相鄰有助於避免重複比對
        nums = sorted(nums)
        # len(nums)-2 原因為為 window 左右邊界留兩位
        for i in range(0, len(nums)-2):
            # 若本位與前一位相同，由於是重複比對因此直接跳過本次迴圈
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 設定 window 左右邊界
            l, r = i+1, len(nums)-1
            while l < r:
                # 利用本位配合window左右邊界來搜尋
                s = nums[i] + nums[l] + nums[r]
                # 若 s 已小於 0 表示左邊界對於右邊界已經過小
                # 代表右邊界若繼續移動 s 只會更小，因此左邊界右移一位
                if s < 0:
                    l +=1 
                # 若 s 已大於 0 表示右邊界對於左邊界已經過大
                # 代表左邊界若繼續移動 s 只會更大，因此右邊界左移一位
                elif s > 0:
                    r -= 1
                # 已得到欲求結果，因此左右邊界各向中心移動
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # 若左邊界下一位與目前左邊界相同，由於是重複比對，左邊界右移一位
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # 若右邊界下一位與目前右邊界相同，由於是重複比對，右邊界左移一位
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        
        return ans
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.threeSum([-1, 0, 1, 2, -1, 4]))