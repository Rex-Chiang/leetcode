class Solution:
    def minIncrementForUnique(self, A):
        if not A:
            return 0
        
        A.sort()
        count = 0
        cur = A[0]
        
        for i in A[1:]:
            if i <= cur:
                cur += 1
                # 此差即為需 +1 的次數
                count += cur - i
            else:
                cur = i
        return count
        
if __name__ == "__main__":
    s = Solution()
    print(s.minIncrementForUnique(A = [3,2,1,2,1,7]))