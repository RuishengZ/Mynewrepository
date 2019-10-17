class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Basically, this problem is same as the 36th problem, with
        # an additional DFS algorithm
        
        # Eliminate the extreme cases:
        if not board:
            return False
        
        # Create a solver (function) for this problem
        self.solver(board)
        
    def solver(self, board):
        
        # Start with checking every block in the board 
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1,10):
                        if self.isValid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solver(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    
    def isValid(self, board, row, col, c):
        # For every input point's coordinate (row, col), we need to look through
        # all columns of the row "row", and all rows of the column "col"
        
        for i in range(9):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: return False
        return True
            
    