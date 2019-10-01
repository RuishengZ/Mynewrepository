class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Create an initial dictionary to store the progress of the evolution
        mapping = {beginWord: 1}
        
        # Exclude duplicate words to avoid stepping into a corner
        wordList = set(wordList)
        
        # Initialize the step (it's 2 because the beginWord is the first step)
        step = 2
        
        lis = [beginWord]
        while lis:
            new_lis = []
            for i in lis:
                if i == endWord:
                    return mapping[i]
                for j in range(len(i)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        # Using combination to detect the next word
                        temp = i[:j] + letter + i[j + 1:]
                        if temp not in mapping and temp in wordList:
                            mapping[temp] = step
                            new_lis.append(temp)
            lis = new_lis
            step += 1
             
            
        # return false if there is no feasible word 
        return 0
            
            
                    