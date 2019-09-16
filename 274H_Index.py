class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # Sort the list with reversed order
        citations.sort(reverse = True)
        
        # Initialize the value of h-index (threshold)
        h_index = 0
        
        # Solve for the value of h-index
        for i in citations:
            if i > h_index:
                h_index += 1
        return h_index