class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # Exclude extreme situations
        if sum(nums) == 0 or len(nums) == 0:
            return "0"
        
        # Use bubble method
        for i in range(len(nums), 0, -1):
            
            # The times of loop are continuously reduced since
            # in each iteration the currently largest number
            # will be settled
            
            for j in range(i - 1):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        return ''.join(list(map(str, nums)))            
        
        