class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # special case
        if len(nums) < 1 or max(nums) <= 0:
            return 1
        
        # Rearrange the sequence
        nums.sort()
        
        # Check if the missing smallest one exists among the elements in list
        for i in range(1, max(nums)):
            if i not in nums:
                return i
        
        # If not, return the value that is 1 more larger than the max(nums)
        return max(nums) + 1
        
        
        
        
