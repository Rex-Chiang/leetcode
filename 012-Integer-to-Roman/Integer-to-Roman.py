class Solution :
    def inToRoman(self, num):
        ans = ""
        num = str(num)
        Roman = {1:"I",5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        
        for n,v in enumerate(num):
            # 計算v的值
            a = int(v)*(10**(len(num)-n-1))
            # 計算v的位數
            b = 10**(len(num)-n-1)

            if a in Roman:
                ans += Roman[a]

            elif a//b <= 3:
                    ans += (Roman[b]) * (a//b)
            # 大於5小於9者要進位
            else:
                k = (a//b)-5
                
                ans += (Roman[5*b])
                ans += (Roman[b] * k)
        
        return ans
    
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.inToRoman(1994))