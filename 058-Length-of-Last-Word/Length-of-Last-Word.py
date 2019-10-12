class Solution:
    def lengthOfLastWord1(self, s):
        if not s.split():
            return 0
        return len(s.split()[-1])
    
    def lengthOfLastWord2(self, s):
        r = -1
        # r指標用以避免右側空格
        while r >= -len(s) and s[r] == " ":
            r-=1
        # 跳過右側空格後 l 從 r 的位置再開始計算
        l = r
        while l >= -len(s) and s[l] != " ":
            l-=1
        return r - l
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord1(s = "Hello World"))
    print(s.lengthOfLastWord2(s = "a "))
    