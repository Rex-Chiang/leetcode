class Solution:
    # 直接建立照表
    def multiply1(self, num1, num2):
        if (num1 == "0") or (num2 == "0"):
            return str(0)
        
        NumsDict = {"0":0, "1":1, "2":2,
                    "3":3, "4":4, "5":5,
                    "6":6, "7":7, "8":8,
                    "9":9}
        
        n1 = 0
        n2 = 0
        zero1 = len(num1)-1
        zero2 = len(num2)-1
        # 由zero1 & zero2進位
        for i in num1:
            n1+=NumsDict[i]*(10**zero1)
            zero1-=1
            
        for i in num2:
            n2+=NumsDict[i]*(10**zero2)
            zero2-=1
            
        return str(n1*n2)
    
    # 由函數ord回傳對應的Unicode字元 (以ord("0")為基準)
    def multiply2(self, num1, num2):
        if (num1 == "0") or (num2 == "0"):
            return str(0)
        
        n1 = 0
        n2 = 0
        zero1 = len(num1)-1
        zero2 = len(num2)-1
        # 由zero1 & zero2進位
        for i in num1:
            n1 += (ord(i)-ord("0"))*(10**zero1)
            zero1-=1
            
        for i in num2:
            n2 += (ord(i)-ord("0"))*(10**zero2)
            zero2-=1
            
        return str(n1*n2)
        
if __name__ == "__main__":
    s = Solution()
    print(s.multiply2(num1 = "123", num2 = "456"))
    