class Solution:
    def LinearScan(self, nums, target):
        # 先至左掃描
        for l in range(0, len(nums)):
            if nums[l]== target:
                left_index = l
                break
        # 迴圈與 else 搭配
        else:
            return [-1, -1]
        # 再至右掃描
        for r in range(len(nums)-1, -1, -1): 
            if nums[r]== target:
                right_index = r
                break
            
        return [left_index, right_index]
    
    def BinarySearch(self, nums, target):
        def search(n):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                # 若 mid >= target, hi向左移動
                # 反之 lo 向右移動                
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        # target+1 為了跳過 left index , 再-1因 target 有+1
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
                
            
if __name__ == "__main__":
    s = Solution()
    print(s.LinearScan(nums = [5, 7, 7, 8, 8, 10], target = 8))
    print(s.BinarySearch(nums = [5, 7, 7, 8, 8, 10], target = 8))
    