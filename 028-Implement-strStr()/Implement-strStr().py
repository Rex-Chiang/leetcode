class Solution:
    def strStr(self, haystack, needle):
        # 只到 len(haystack) - len(needle)因不可能會再多於這個長度
        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
if __name__ == "__main__":
    s = Solution()
    print(s.strStr(haystack = "hello", needle = "ll"))
    