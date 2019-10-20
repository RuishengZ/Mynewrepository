class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # We will use DFS method to solve this problem
        
        # Eliminate the extreme cases:
        if not nums or len(nums) < 2:
            return 0
        
        # We set several variables to record the steps we need in order to
        # reach the last index, the current area we are allowed to move, how many steps
        # we could move within the current area and the max area
        # involved which based on the current position and the steps it can move.
        step = 0
        curArea = 0
        i = 0
        maxArea = 0
        
        while curArea - i + 1 > 0: # make sure we have arrived at all indices that
        # contained in the current area. +1 in the end because we need to at least
        # move 1 step
            step += 1
            for j in range(i, curArea + 1):
                maxArea = max(maxArea, nums[j] + j)
                if maxArea >= len(nums) - 1:
                    return step
                i = j
            curArea = maxArea
        
        return 0
            
            
        
        