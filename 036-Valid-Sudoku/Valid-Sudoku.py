class Solution:
    def isValidSudoku(self, board):
        Set = set()
        for i in range(0,9):
            for j in range(0,9):
                # 若元素為"."則跳過
                if board[i][j]!='.':
                    cur = board[i][j]
                    # 以列、行、九宮格搭配 index成 tuple作 Key，檢查是否重複
                    # //3為九宮格的編號 : 0,1,2
                    if (i,cur) in Set or (cur,j) in Set or (i//3,j//3,cur) in Set:
                        return False
                    
                    Set.add((i,cur))
                    Set.add((cur,j))
                    Set.add((i//3,j//3,cur))
        return True

    def isValidSudoku2(self, board):
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))
    # 檢查列
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    # 檢查行(使用zip使其90度翻轉)
    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    # 檢查九宮格(以0, 3, 6作間格)
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
    # 將有數字之元素加入set，若長度不一則代表有重複
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku(board = [["5","3",".",".","7",".",".",".","."],
                                   ["6",".",".","1","9","5",".",".","."],
                                   [".","9","8",".",".",".",".","6","."],
                                   ["8",".",".",".","6",".",".",".","3"],
                                   ["4",".",".","8",".","3",".",".","1"],
                                   ["7",".",".",".","2",".",".",".","6"],
                                   [".","6",".",".",".",".","2","8","."],
                                   [".",".",".","4","1","9",".",".","5"],
                                   [".",".",".",".","8",".",".","7","9"]]))
        