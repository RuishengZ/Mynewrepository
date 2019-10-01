class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # # Approach 1: Try and except
        # try:
        #     return haystack.index(needle)
        # except:
        #    return -1
        
        # Approach 2: Iteration
        if len(needle) == 0:
            return 0
        
        L_hay = len(haystack)
        L_nee = len(needle)
        
        for idx in range(L_hay - L_nee + 1):
            if haystack[idx: idx + L_nee] == needle:
                return idx
        return -1
        