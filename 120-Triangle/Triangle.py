class Solution:
    # Dynamic programming top-down 
    def minimumTotal1(self, triangle):
        if not triangle:
            return 
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                # 遇到首項因僅有單一路徑，直接與前一節點(前一陣列的首項)相加更新
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                # 遇到尾項因僅有單一路徑，直接與前一節點(前一陣列的尾項)相加更新
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                # 選取前一陣列中，有效路徑的兩節點最小值，並相加更新
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        # 由於最後一陣列已是所有路徑的最小可能，因此再選最小
        return min(triangle[-1])
    
    # Dynamic programming bottom-up
    def minimumTotal2(self, triangle):
        if not triangle:
            return 
        # 自倒數第二個陣列開始向上判斷
        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(triangle[i])):
                # 由下一陣列中，有效路徑的兩節點最小值，並相加更新
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
         # 首一陣列已是所有路徑的最小可能
        return triangle[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal1(triangle = [[2],
                                     [3,4],
                                     [6,5,7],
                                     [4,1,8,3]]))
        