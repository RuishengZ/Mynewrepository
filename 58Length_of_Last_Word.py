class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # Get the length of the origin string
        L = len(s)
        
        # Set the counter for the last part 
        space_counter = 0
        counter = 0
        
        for i in range(L - 1, -1, -1):
            if s[i] == ' ':
                space_counter += 1
            else:
                break
        
        # Delete spaces in the end of the string
        s = s[:len(s) - space_counter]
        L_m = len(s)
        
        # Count the number of alphabets of the last word
        for j in range(L_m - 1, -1, -1):
            if s[j] != ' ':
                counter += 1
            else:
                break
                
        return counter
            
        