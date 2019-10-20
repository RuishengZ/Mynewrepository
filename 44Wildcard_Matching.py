class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # We will use a method with time complexity O(n)
        
        # To implement this method, we need to set several pointers
        # to describe the index position in two different strings, as 
        # well as the star point in p str and the corresponding match point in s str
        
        # An example for explanation:
        # s = "bbarc"
        # p = "*c"
        
        pos_s = 0
        pos_p = 0
        star = -1
        match = 0
        
        while pos_s < len(s):
            # Case 1: Two corresponding index positions are equivalent
            
            if pos_p < len(p) and (s[pos_s] == p[pos_p] or p[pos_p] == '?'):
                pos_s += 1
                pos_p += 1
            
            # Case 2: Two corresponding index are different, but we have '*'
            # in p str. In this case, we first assume that '*' hasn't match
            # any character yet, that is: p_pos moves 1 step ahead, but pos_s
            # stays at the same position. The pos_s will move forward if the 
            # current character does not match the next character in p (the last
            # one is '*'), which means the '*' is starting to match (cancel out)
            # the characters that are not contained in p but exist in s.
            
            elif pos_p < len(p) and p[pos_p] == '*':
                star = pos_p
                match = pos_s
                pos_p += 1
                
            elif star != -1:
                # pos_p should not move since it currently has '*' to match
                # other characters in s
                pos_p = star + 1
                
                # pos_s should move forward until the current character in s matches
                # the character in p. Then we back to the case 1.
                match += 1
                pos_s = match
                
            else:
                return False
            
        # The while loop above can make sure that we have already run
        # over the string s, but not the string p because of the existance
        # of '*'. So we need to assure that we have also run all over the 
        # string p, or the rest characters of string p are all '*' because
        # we have already finished scanning s, if p still has other characters
        # rather than '*', then these two strings are definitely different.
        while pos_p < len(p) and p[pos_p] == '*':
            pos_p += 1
            
        if pos_p == len(p):
            return True
        else:
            return False
                
                  
        