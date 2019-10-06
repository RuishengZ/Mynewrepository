class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Eliminate the extreme case:
        if len(nums) <= 1:
            return 
        
        # Normal cases: (Bubble method)
        firstsmall_in = -1
        firstsmall = 0
        firstlarge_in = -1
        
        for i in range(len(nums) - 2, -1, -1): # Start from the end
            if nums[i] < nums[i + 1]:
                firstsmall_in = i
                firstsmall = nums[i]
                break
                
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > firstsmall:
                firstlarge_in = i
                break
        
        if firstsmall_in == -1: # This means the number looks like: 7654321
            # Then we just filp it
            nums = self.partial_flip(nums, 0, len(nums) - 1)
            return
        
        else:
            nums = self.swap(nums, firstsmall_in, firstlarge_in)
            nums = self.partial_flip(nums, firstsmall_in + 1, len(nums) - 1)
            return
        
        
        
        ############################ Function definition 
    def swap(self, nums, i_index, j_index):
        temp = 0
        temp = nums[j_index]
        nums[j_index] = nums[i_index]
        nums[i_index] = temp
        return nums
        
    def partial_flip(self, nums, start_in, end_in):
        while start_in < end_in:
            self.swap(nums, start_in, end_in)
            start_in += 1
            end_in -= 1
        return nums
        
                
        
        
        
        
                
        
        
nums = [3,2,1]
x = Solution()
res = x.nextPermutation(nums)
print(nums)