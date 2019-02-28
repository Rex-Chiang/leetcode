class Solution:
    def isPalindrome(self, x):
        y=x
        if x<0:
            return False
        rev = 0
        
        while x > 0:
            
            rev = rev *10 + x%10
            x = x//10
               
        return rev==y     
        
    
if __name__=="__main__":
    s = Solution
    print(s.isPalindrome(s, 121))
    