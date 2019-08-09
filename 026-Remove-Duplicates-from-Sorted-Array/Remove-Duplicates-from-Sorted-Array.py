class Solution(object):
    def removeDuplicates(self, nums):
        point = 0
        
        for num in nums[1:]:
            if num != nums[point]:
                point += 1
                # 以置換的方式就能直接進行比對
                nums[point] = num
        return point+1


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1,1]))
    print(s.removeDuplicates([1,2,3,3]))