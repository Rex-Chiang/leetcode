class Solution:
    def countAndSay(self, n):
        ans = '1'
        # 因已從 ans = "1" 開始因此迴圈只需n-1次
        for _ in range(n-1):
            # cur為判定目前為 1或 2
            # tmp用以暫存目前計數狀況
            cur, tmp, count = ans[0], '', 0
            
            for i in ans:
                # 若元素不變則繼續加總
                if cur == i:
                    count += 1
                # 若元素轉變則暫存目前計數狀況至tmp，並將cur及count重置為新的狀況
                else:
                    tmp += str(count) + cur
                    # 元素轉變為 1或 2
                    cur = i
                    count = 1
                    
            tmp += str(count) + cur
            ans = tmp
        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(n = 5))