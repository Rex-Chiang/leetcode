class Solution:
    def spiralOrder(self, matrix):
        # 不能使用 if matrix 因其無法做到當False時return前一層遞迴的return
        # The expression x and y :
        # first evaluates x; if x is false, its value is returned;
        # otherwise, y is evaluated and the resulting value is returned.
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        
if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder(matrix = [[ 1, 2, 3 ],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9 ]]))