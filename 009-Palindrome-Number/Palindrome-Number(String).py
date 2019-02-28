class Solution:
    def isPalindrome(self, x):
        y = str(x)[::-1]
        if str(x)==y:
            return True
        else:
            return False
    
    
    
if __name__=="__main__":
    s = Solution
    print(s.isPalindrome(s, 121))
    