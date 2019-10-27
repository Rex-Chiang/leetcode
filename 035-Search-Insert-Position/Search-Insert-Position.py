class Solution:
    # Loop Search
    def searchInsert1(self, nums, target):
        index = 0
        
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        
        for i in nums:
            if i == target:
                return index
            elif nums[index] < target < nums[index+1]:
                return index+1
            else:
                index += 1
    # Binary Search
    def searchInsert2(self, nums, target):
            l, r = 0, len(nums)-1
            
            while l <= r:
                mid = (l+r)//2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            return l
        
if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert2(nums = [1,3,5,6], target = 5))
    