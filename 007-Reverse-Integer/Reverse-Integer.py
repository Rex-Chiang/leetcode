class Solution:
    def reverse(self, x):
        
        if x>=0:
            x = int(str(x)[::-1])
        else:
            x = int("-"+str(abs(x))[::-1])
            
        if x > 2**(31) or x < -2**(31):
            x=0
        
        return x
        
if __name__=='__main__':
    s = Solution
    print(s.reverse(s, 123))