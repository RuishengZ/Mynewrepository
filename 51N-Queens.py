class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # This is a classic backtracking problem plus with dfs
        
        # We start with eliminating extreme cases
        if n == 0:
            return []
        
        # For other cases, we use traditional dfs:
        # We start with initializing the board, which means filling up the
        # board with '.':
        board = [['.' for j in range(n)] for i in range(n)]
        
        # Initialize the col, left, right diagonals and result vectors:
        
        # These three vectors are used to avoid duplications on col, left and
        # right diagonals
        col = []
        leftd = []
        rightd = []
        
        result = []
        
        # Implementing dfs function:
        
        result = self.dfs(n, 0, board, col, leftd, rightd, result)
        return result
    
    # Define the dfs function:
    # Variable 'level' represents the row index you are in
    def dfs(self, dim, level, chess_board, col, leftd, rightd, res):
        # Output the result when the last row can be filled
        if level == dim:
            temp = []
            for i in range(dim):
                temp.append("".join(chess_board[i]))
            res.append(temp)
            
        # Put all the Queens on chess board before ending (without repeating on
        # column, left and right diagonals):
        for i in range(dim):
            if (i not in col) and ((level - i) not in leftd) and ((level + i) not in rightd):
                col.append(i)
                leftd.append(level - i)
                rightd.append(level + i)
                chess_board[level][i] = 'Q'
                self.dfs(dim, level + 1, chess_board, col, leftd, rightd, res)
                
                # Back one step
                chess_board[level][i] = '.'
                col.remove(i)
                leftd.remove(level - i)
                rightd.remove(level + i)
        return res
        
                
        