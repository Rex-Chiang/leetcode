class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        tmp = [1]
        res = []
        
        while len(res) < rowIndex + 1:
            res = []
            # 前後加 0以利兩兩相加
            tmp = [0] + tmp + [0]
            
            for i in range(0, len(tmp)-1):
                res.append(tmp[i]+tmp[i+1])
            
            tmp = res
            
        return res
        
if __name__ == "__main__":
    s = Solution()
    print(s.getRow(rowIndex = 5))