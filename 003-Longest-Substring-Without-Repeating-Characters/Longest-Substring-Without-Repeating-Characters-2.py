class Solution:
    def lengthOfLongestSubstring(self,s):
        window = 0 # 窗口大小
        left = 0 # 左邊界
        right = 0 # 右邊界
        Dict = {} # 紀錄位置
        
        while right < len(s):
            if s[right] in Dict:
                # 因要調整邊界，先紀錄當前窗口大小
                window = max(window, right-left)
                # 調整左邊界
                if Dict[s[right]] >= left:
                    left = Dict[s[right]] + 1
            # 新增或調整元素位置    
            Dict[s[right]] = right
            # 調整右邊界
            right+=1
        return max(window,  right-left)
    
if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring("abcabcbb"))