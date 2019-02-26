class Solution:
    def twoSum(self, nums, target):
    
        s =[]
            
        for i in range(0, len(nums)-1):
            for j in range(i,len(nums)-1):
                if nums[i]+nums[j+1] == target:
                    s.append(i)
                    s.append(j+1)
                
        return s
        
if __name__=='__main__':
    s = Solution
    print(s.twoSum(s, [2,7,11,15],9))
    
    