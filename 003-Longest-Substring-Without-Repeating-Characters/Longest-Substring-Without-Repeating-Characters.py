class Solution:
    def lengthOfLongestSubstring(self,s):       
        a=""
        b=""        
        for i in range(0, len(s)):            
            for j in range(i, len(s)):               
                if s[j] not in b:
                    b += s[j]
               
                elif (s[j] in b):
                    break
                
            if len(b)>len(a):
                a = b
            b = ""
            
        return len(a)
    
if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring("abcabcbb"))