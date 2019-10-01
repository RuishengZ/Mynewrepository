class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # This is a typical dynamic programming problem
        
        current_sum = 0
        current_max = nums[0]
        for i in nums:
            current_sum = max(current_sum + i, i)
            if current_sum > current_max:
                current_max = current_sum
        return current_max
        
        