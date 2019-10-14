class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # The loop will contain 9x9 times operation. For each operation:
        # One elements of a row (9 elements), a column (9 elements) and a cube (3x3)
        # will be judged.
        
        
        for i in range(len(board[0])):
            dic_row = {}
            dic_col = {}
            dic_cube = {}
            for j in range(len(board[0])):
                # column judgement:
                if board[i][j] != '.' and board[i][j] in dic_row: 
                    return False
                else:
                    dic_row[board[i][j]] = 1
                
                # row judgement:
                if board[j][i] != '.' and board[j][i] in dic_col:
                    return False
                else:
                    dic_col[board[j][i]] = 1
                    
                # cube judgement: Since the given input can be seen
                # as a 3x3 box, each sub-box is also 3x3 scaled.
                # Our judgement operation follows the order:
                # 1 2 3
                # 4 5 6
                # 7 8 9
                row_part = 3 * (i//3)
                col_part = 3 * (i % 3)
                
                if board[row_part + (j // 3)][col_part + (j % 3)] != '.' and board[row_part + (j // 3)][col_part + (j % 3)] in dic_cube:
                    return False
                else:
                    dic_cube[board[row_part + (j // 3)][col_part + (j % 3)]] = 1
                    
        return True