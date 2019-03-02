class Solution:
    def longestCommonPrefix(self, strs):      
        # 若為空集合或有空元素返回" "
        if (len(strs) == 0) or ("" in strs):
            return ""
        # 若只有單一元素返回本身
        elif len(strs) == 1:
            return strs[0]       
        # 兩兩比對第一個字母，比對完後若為相同，刪除第一個字母
        else:            
            ps = ""
            while True :                
                for i in range(0, len(strs)-1):
            
                    if strs[i][0] == strs[i+1][0]:
                        strs[i] = strs[i].replace(strs[i][0],"",1)
                        if (i+2) == len(strs):
                            ps += strs[i+1][0]
                            strs[i+1] = strs[i+1].replace(strs[i+1][0],"",1)

                    else:                        
                        return ps
                    
                if "" in strs:
                            return ps
    
if __name__ == "__main__":
    s = Solution
    print(s.longestCommonPrefix(s,["a","a","a"]))