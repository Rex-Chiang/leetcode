class Solution:
    def longestCommonPrefix(self, strs):      
        n = 0
        
        if len(strs) == 0 or strs[0] == "":
            return ""
        
        elif len(strs) == 1:
            return strs[0]
        
        elif "" in strs:
            return ""
        
        elif len(strs) == 2:
            ps = strs[0]
            low = min(len(strs[0]),len(strs[1]))
            while (n <= low) and (min(len(strs[0]),len(strs[1]))!=0) :
                for i in range(0, min(len(strs[0]),len(strs[1]))):
                    if (i != 0) and (n == 0):
                        break
                    if (strs[0].find(strs[1][i]) >= 0) and (strs[0].find(strs[1][i]) == strs[1].index(strs[1][i])):
                        #print(i)
                        n +=1
                        strs[0] = strs[0].replace(strs[0][0],"",1)
                        strs[1] = strs[1].replace(strs[1][0],"",1)
                        break
                if (n == 0) or ("" in strs) or (strs[0][0] != strs[1][0]):
                    break
            if n==0:
                ps=""
            return ps[:n]
        
        elif len(strs)>2:            
            ps = strs[0]        
            while (n % (len(strs)-1) ==0) and (min(len(strs[0]),len(strs[1]))!=0):
                for i in range(0, len(strs)-1):
                    if (strs[i].find(strs[i+1][0]) >= 0) and (strs[i].find(strs[i+1][0]) == strs[i+1].index(strs[i+1][0])):
                        n +=1
                        strs[i] = strs[i].replace(strs[i][0],"",1)
                        if (i+2) == len(strs):
                            strs[i+1] = strs[i+1].replace(strs[i+1][0],"",1)
                if (n == 0) or ("" in strs) or (strs[0][0] != strs[1][0]):
                    break

            if (n % 2 != 0) and (len(strs)%3==0):
                n-=1
            if n==0:
                ps=""
            return ps[:n//(len(strs)-1)]
    
    
if __name__ == "__main__":
    s = Solution
    print(s.longestCommonPrefix(s,["flower","flow","flight"]))