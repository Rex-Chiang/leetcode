class Solution:
    def groupAnagrams(self, strs):
        strDict = {}
        # 以排序過的字串作為同形字的key
        for str in strs:
            key = "".join(sorted(str))
            # key = tuple(sorted(i))
            # Array is not hashable, which means it is not allowed to be a key.
            # Tuple could be a key.
            
            if key not in strDict:
                strDict[key] = [str]
            else:
                strDict[key].append(str)
   
        return strDict.values()
    
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
        