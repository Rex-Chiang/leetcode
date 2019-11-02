class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先顛倒
        # [[7, 8, 9], 
        #  [4, 5, 6], 
        #  [1, 2, 3]]
        # 再 zip 結合 (*用以unpack)
        # 因 zip 後為tuple，使用 map 轉為 list 型式
        matrix[:] = map(list, zip(*matrix[::-1]))

if __name__ == "__main__":
    s = Solution()
    print(s.rotate(matrix  = [[1,2,3],
                              [4,5,6],
                              [7,8,9]]))