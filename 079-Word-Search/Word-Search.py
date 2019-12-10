class Solution:
    def exist(self, board, word):
        # 若board為空
        if not board:
            return False
        # 找首項，若非首項則 False即 return
        for r in range(len(board)):
            for c in range(0, len(board[0])):
                if self.search(r, c, board, word):
                    return True
        return False
    
    def search(self, r, c, board, word):
        # 若 word檢查完或為空
        if len(word) == 0:
            return True
        # 若超過 index或找不到字
        if (r < 0) or (r >= len(board)) or (c < 0) or (c >= len(board[0])) or (word[0] != board[r][c]):
            return False
        # 紀錄已走
        board[r][c] = " "
        # 四種方向
        result = self.search(r+1, c, board, word[1:]) or self.search(r-1, c, board, word[1:]) \
        or self.search(r, c+1, board, word[1:]) or self.search(r, c-1, board, word[1:])
        
        board[r][c] = word[0]
        
        return result
        
if __name__ == "__main__":
    s = Solution()
    print(s.exist(board = [['A','B','C','E'],
                           ['S','F','C','S'],
                           ['A','D','E','E']], word = "ABCCED"))