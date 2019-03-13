class Solution:
    
    def searchSides(self, s, l, r):
            # 左右邊界不得超過原字串長度，且先確認中心點兩側值是否相等
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 由中心向左右擴張
                l -= 1
                r += 1
                
            return r - l - 1
    
    def longestPalindrome(self, s):
        
        max_lenth = 0        
        if len(s) <= 1:
        
            return s
        
        ans = ''
        
        for i in range(len(s)):
            # 以一個為中心，因此子字串為奇數
            windowODD = self.searchSides(s, i, i)
            # 以兩個為中心，因此子字串為偶數
            windowEVEN = self.searchSides(s, i, i + 1)
            
            tmp_lenth = max(windowODD, windowEVEN)
            
            if tmp_lenth > max_lenth:
                max_lenth = tmp_lenth
                # 取出目前中心為一個的最長子字串
                if tmp_lenth % 2 == 1:
                    ans = s[ i - (tmp_lenth//2) : i + (tmp_lenth//2) + 1]
                # 取出目前中心為兩個的最長子字串
                else:
                    ans = s[ i + 1 - (tmp_lenth//2) : i + 1 + (tmp_lenth//2)]
        
        return ans
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))