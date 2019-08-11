class Solution(object):
    def removeElement(self, nums, val):
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                # 由置換的方式來檢測未檢測的元素
                nums[l], nums[r], r = nums[r], nums[l], r - 1
            else:
                l +=1
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], val = 2))