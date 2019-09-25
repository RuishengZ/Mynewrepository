class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Extreme case:
        if len(s) == 0:
            return ""
        
        # Otherwise, we use Dynamic programming:
        max_s = s[0]
        max_len = len(s[0])
        L = len(s)
        
        # Create a 2-dimensional matrix to cover all cases of strings
        dp = [[0]*L for i in range(L)]
        
        # DP starts (Backward)
        # 1. The head and the tail must be equal
        # 2. i and j cannot be reversed
        # 3. The last substring must also be palindromic
        # 4. j - i + 1, plus 1 because of the index problem in python
        # for i in range(L - 1, -1, -1):
        #     for j in range(i, L):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]): 
        #             dp[i][j] = 1
        #             if dp[i][j]:
        #                 if j - i + 1 > max_len:
        #                     max_len = j - i + 1
        #                     max_s = s[i:j + 1]
        # return max_s
        
        # DP starts (Forward)
        for i in range(L):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1]): 
                    dp[i][j] = 1
                    if dp[i][j]:
                        if i - j + 1 > max_len:
                            max_len = i - j + 1
                            max_s = s[j:i + 1]
        return max_s