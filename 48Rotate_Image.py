class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Any type of rotation problem can be solved by different
        # combinations of filpping the elements
        # according to diagonal or other axes (plural form of axis).
        # This problem is relatively easy, which we only need to firstly
        # filp over the elements according the diagonal and then filp again
        # according to the axis in the middle of the matrix
        # E.g: [
        #       [1,2,3]
        #       [4,5,6]    
        #       [7,8,9]
        #              ] In this case, the filps are based on
        # 1                   4
        #   5       and then  5
        #     9               6
        
        
        # Firstly, we filp the elements in matrix based on diagonal
        # that is matrix[i][j] to matrix[j][i]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        
        # Then, we filp the elements in both sides of the middle axis
        # that is matrix[i][j] to matrix[i][len(matrix) - 1 - j], where
        # len(matrix) - 1 is the last element of each row and only half
        # of elements in a row should be operated (except the elements
        # in the middle line)
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix) - 1 - j]
                matrix[i][len(matrix) - 1 - j] = temp
            