class Solution:
    def romanToInt(self, s):
        k1_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        k2_dic = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        k3_dic = {'III':3,'VVV':15,'XXX':30,'LLL':150,'CCC':300,'DDD':1500,'MMM':3000}
        
        n = 0
        
        k1 = []
        k2 = []
        k3 = []
      
        for i in range(0, len(s)):
            if (len(k3)+2) <= (len(s)-1):
                k3.append(s[i]+s[i+1]+s[i+2])

        for i in k3:
            if i in k3_dic.keys():
                n += k3_dic[i]
                s = s.replace(i,"")

        for i in range(0, len(s)):
            if (len(k2)+1) <= (len(s)-1):
                k2.append(s[i]+s[i+1])

        for i in k2:
            
            if i in k2_dic.keys():
                n += k2_dic[i]
                s = s.replace(i,"")
        
        for i in range(0, len(s)):
            k1.append(s[i])

        for i in k1:
            if i in k1_dic.keys():
                n += k1_dic[i]
        
        return n
    
    
    
    
if __name__ == "__main__":
    sol = Solution
    print(sol.romanToInt(sol, 'MCMXCIV'))