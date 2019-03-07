class Solution:
    def z(self, s, n):
        z = [] # 將Z型攤平的陣列
        m = n-2 # Z型的拐彎處字元數
        pointer = n # 辨別在Z型的平行處還是拐彎處
        while s != "":
            # 在Z型的平行處
            if pointer == n:
                # 在最後剩餘字元數不達n時補齊空白
                if len(s) < n:
                    z.append(s+((n-len(s))*" "))
                    s = ""
                # 擷取n個字元作Z型的平行處
                else:
                    z.append(s[:n])
                    s = s[n::]                          
                pointer = m
                
            # 在Z型的拐彎處
            elif pointer == m:
                # 擷取m個字元並補齊空白作Z型的拐彎處
                z.append((" "+s[:m]+(n-len(s[:m])-1)*" ")[::-1])
                # 由於Z型的拐彎處擷取方向為相反因此將字串顛倒
                s = s[m::]                
                pointer = n
        return z
    
    def convert(self, s, numRows):
        n = numRows# Z型的平行處字元數
        
        if n == 1:
            return s
        
        z = self.z(s,n)

        ans = ""
        # 將Z型攤平的陣列無視空白整合成字串
        for i in range(0,n):
            for j in z:
                if j[i] != " ":
                    ans+=j[i]        
        return ans
    
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.convert(s="PAYPALISHIRING", numRows=4))
    