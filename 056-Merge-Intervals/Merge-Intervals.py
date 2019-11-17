class Solution:
    def merge(self, intervals):
        out = []
        # 照每個區間之首排序
        for i in sorted(intervals, key=lambda x:x[0]):
            # 合併區間(直接更新尾段)
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            # 加入結果
            else:
                out += [i]
        return out
        
if __name__ == "__main__":
    s = Solution()
    print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
        