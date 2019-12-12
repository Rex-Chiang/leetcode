class Solution:
    # Too slow
    def combine(self, n, k):
        nums = [x for x in range(1, n+1)]
        result = []
        self.dfs(k = k, nums = nums, path = [], result = result)
        return result
        
    def dfs(self, k, nums, path, result):
        
        if len(path) == k:
            result.append(path)
            return
            
        for i in range(0, len(nums)):
            self.dfs(k, nums[i+1:], path + [nums[i]], result)
            
    def combine1(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            # One combination has k numbers, and currently we already have l numbers,
            # so we need to find another k-l numbers. 
            # Since we insert the numbers into stack in the ascending order, 
            # we want to make sure that there are enough larger numbers to be inserted. 
            # From x to n, 
            # there are n-x+1 numbers that are larger than the numbers in the current stack. 
            # So if n-x+1 < k-l, it means that not enough larger numbers to be inserted, so we track back.
            if l == k or n-x+1 < k-l:
                if not stack:
                    return ans
                # pop()後 stack少一元素
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
            
if __name__ == "__main__":
    s = Solution()
    print(s.combine1(n = 4, k = 2))