class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 0:
            return []

        tmp = [1]
        tmp_res = []
        res = [[1]]
        
        while len(tmp_res) < numRows:
            tmp_res = []
            tmp = [0] + tmp + [0]
            
            for i in range(0, len(tmp)-1):
                tmp_res.append(tmp[i]+tmp[i+1])
            
            tmp = tmp_res
            res.append(tmp_res)
            
        return res
        
if __name__ == "__main__":
    s = Solution()
    print(s.generate(numRows = 5))