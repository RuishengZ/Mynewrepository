class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # There is no simple algorithm to solve this problem, thus it's
        # just a realization problem
        
        # We are going to use two dictionaries here, one is fixed, another
        # is flexible
        
        # Before dealing with normal cases, we firstly eliminate some 
        # extreme cases:
        if not s or not words or len(s) == 0 or len(words) == 0:
            return []
        
        # For the normal cases, we create a stable dictionary to store
        # all words that appear in words
        w_table = {}
        for word in words:
            w_table[word] = 0
        for word in words:
            w_table[word] += 1
            
        # We start to go through all elements in s. However the number of 
        # loop time should be len(s) - n*m + 1 (+1 because of the index problem),
        # where n is the number of word contained in vector words and m 
        #is the number of character of each word. This is because the whole 
        # string has the length of n*m.
        result = []
        n = len(words)
        m = len(words[0])
        for i in range(len(s) - n*m + 1):
            temp_table = w_table.copy()
            # We use a viriable to record the rest number of words in the
            # given vector. Also, we need a pointer that always starts from
            # the current position 'i', and ends up at j + m.
            k = n
            j = i
            while k > 0:
                temp_string = s[j:j + m]
                if temp_string not in temp_table or temp_table[temp_string] < 1:
                    break
                temp_table[temp_string] -= 1
                k -= 1
                j += m
            # If all words have been matched, then index 'i' is an desire
            # start point
            if k == 0:
                result.append(i)
        
        return result
            
            
            
            
        