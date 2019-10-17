class Solution:
    def trap(self, height: List[int]) -> int:
        
        # We first need to define 2 pointers and 2 temporary variables to
        # save the value of the current maximum height of wall
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        result = 0
        
        while (left < right):  # not reversible
            # Water can be stored only when there is a closed
            # space, which means wall exists in both the right and
            # left sides. The capacity of any closed space to store 
            # water depends on the lowest height side. For example:
            # if the height of the left side is lower than the right
            # side, then we just need to focus on the left side because
            # water won't leak out at the another side. In this case we need to 
            # check if there exists a downward edge at the left
            # side. The space is created if such edge exists. Same way to
            # the right side.
            
            if height[left] < height[right]:
                max_left = max(height[left], max_left)
                result += max_left - height[left]
                left += 1
                
            else:
                max_right = max(height[right], max_right)
                result += max_right - height[right]
                right -= 1
                
        return result
        