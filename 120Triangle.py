class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Initialize the vector variable for dynamic programming
        dp_v = triangle[-1]
        L = len(triangle)
        
        # The DP process starts from the second to last row
        # L - 2 means we don't need to calculate for the last row (start point)
        # and the first row (end point)
        
        for i in range(L - 2, -1, -1):
            for j in range(i + 1):
                dp_v[j] = min(dp_v[j], dp_v[j + 1]) + triangle[i][j]
        
        # The first element will be the mimimum sum 
        return dp_v[0]
            
            
            