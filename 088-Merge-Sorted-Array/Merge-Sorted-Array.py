class Solution:
    def merge(self, nums1, m, nums2, n):
        # 合併兩數組
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]
        # 插入排序法
        for i in range(1, len(nums1)):
            tmp = nums1[i]
            j = i-1
            while (j >= 0) and (tmp < nums1[j]):
                nums1[j+1] = nums1[j]
                j -= 1
            nums1[j+1] = tmp
            
        return nums1
    
    # 非合併之方法
    def merge1(self, nums1, m, nums2, n):
        while n > 0:
            # 若nums2最大值 >= nums1最大值，則nums2最大值取代nums1最右邊之0
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # # 若nums2最大值 < nums1最大值，則nums1最大值取代nums1最右邊之0
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
    
if __name__ == "__main__":
    s = Solution()
    print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))