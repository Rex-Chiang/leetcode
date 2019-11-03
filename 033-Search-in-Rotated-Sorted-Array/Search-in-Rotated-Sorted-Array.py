class Solution:
    def search(self, nums, target):
        # 若nums為空
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        # 基本概念為將nums分為兩部分
        while low <= high:
            mid = (low + high) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                # [小:target:mid][小:大]
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                # [小:mid][小:target:大]
                else:
                    low = mid + 1
            else:
                # [小:mid][小:target:大]
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                # [小:target:mid][小:大]
                else:
                    high = mid - 1

        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.search(nums = [4,5,6,7,0,1,2], target = 0))