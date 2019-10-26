class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # In this problem, we run through all characters of every words
        # in the given list, calculating the numerical value of each word
        # by using ASCII code to judge if it's the same word.
        
        # We first eliminate some extreme cases:
        if not strs or len(strs) == 0:
            return []
        
        
        # We create a dictionary and use ASCII code to deal with the normal
        # cases
        Map = {}
        for word in strs:
            # Use a list to record the characters that appear in each word
            table = [0 for i in range(26)]
            for character in word:
                table[ord(character) - ord('a')] += 1
            
            # Create an unique string as a label for each word
            s = ""
            for i in range(len(table)):
                if table[i] != 0:
                    s += str(table[i]) + str(chr(i + ord('a')))
        
            # Make the category
            if s in Map:
                Map[s].append(word)
            else:
                Map[s] = []
                Map[s].append(word)
                
        return Map.values()
        
                    
                
                
        