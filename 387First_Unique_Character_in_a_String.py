class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # In other python environment, one has to do: import collections first 
        d = collections.Counter(s)
        
        # find the index
        for key, value in d.items():
            if value == 1:
                return s.index(key)
            
        return -1