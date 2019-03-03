class Solution:
    def twoSum(self, nums, target):    
        s=[]
        for i in enumerate(nums):
            if (target-i[1] in nums):
                # 兩相同值組合target                
                if (nums.count(target/2) == 2):
                    s.append(i[0])
                # 兩相異值組合target
                elif (i[1] != target/2):                
                    s.append(i[0])
        return s
        
if __name__=='__main__':
    s = Solution
    print(s.twoSum(s, [2,7,11,15],9))