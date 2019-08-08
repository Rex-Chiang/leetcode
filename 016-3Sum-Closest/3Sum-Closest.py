class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        temp = 100000000
        for i in range(0, len(nums)-2):
            # 設定 window 左右邊界
            l = i+1
            r = len(nums)-1
            # nums[i] != nums[i-1] 若本位與前一位相同避免重複比對
            if (i == 0) or (nums[i] != nums[i-1]):
                while l<r:
                    s = nums[i] + nums[l] + nums[r]
                    # key point
                    if s == target:
                        return s
                    elif abs(s-target) <= temp:
                        # temp用於暫存目前加總與目標值之差距
                        temp = abs(s-target)
                        result = s
                        # 若 (s-target) 已小於 0 表示左邊界對於右邊界已經過小
                        # 代表右邊界若繼續移動 s 只會更小，因此左邊界右移一位
                        if (s-target) <= 0:
                            l+=1
                        # 若 (s-target) 已大於 0 表示右邊界對於左邊界已經過大
                        # 代表左邊界若繼續移動 s 只會更大，因此右邊界左移一位
                        elif (s-target) > 0:
                            r-=1
                    elif abs(s-target) > temp:
                        # 若 (s-target) 已小於 0 表示左邊界對於右邊界已經過小
                        # 代表右邊界若繼續移動 s 只會更小，因此左邊界右移一位
                        if (s-target) <= 0:
                            l+=1
                        # 若 (s-target) 已大於 0 表示右邊界對於左邊界已經過大
                        # 代表左邊界若繼續移動 s 只會更大，因此右邊界左移一位
                        elif (s-target) > 0:
                            r-=1
        return result
                        
        
if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest(nums = [1,1,-1,-1,3], target = 1))