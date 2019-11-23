class Solution:
    # 可能會有重複檢查的情況
    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        
        zero = set()

        for i in range(0, R):
            # 若此列有0則遍尋此列
            if 0 in matrix[i]:
                for j in range(0, C):
                    # 將為0的行位置紀錄至zero
                    if matrix[i][j] == 0:
                        zero.add(j)
                    # 再將此列元素都化為0
                    matrix[i][j] = 0
        # 將zero所記錄的行位置都化為0
        for i in range(0, R):
            for j in zero:
                matrix[i][j] = 0
                
    # 利用只記錄行列第一個元素(2 flags)避免重複檢查
    def setZeroes2(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        # 由於每次需標示2 flags，但matrix[0][0]會重複，因次利用is_col來表示其一 flag
        is_col = False
        
        for i in range(0, R):
            if matrix[i][0] == 0:
                is_col = True
            # 因第一行及第一列作為flags，從第二行及第二列開始
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        # 利用2 flags將元素化為0    
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        # 若第一列須為0      
        if matrix[0][0] == 0:
            for j in range(0, C):
                matrix[0][j] = 0
        
        # 若第一行須為0        
        if is_col:
            for i in range(0, R):
                matrix[i][0] = 0