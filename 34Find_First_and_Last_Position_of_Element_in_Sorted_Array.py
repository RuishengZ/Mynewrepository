class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Since the runtime complexity must be in the order of
        # O(log n), so this is a binary-searching problem.
        # Here, binary means we divide each sub-list to two parts
        # to find the target number part.
        
        # Eliminate the extreme cases:
        if not nums or len(nums) == 0:
            return[-1, -1]
        
        # As for normal cases, we need to develop two functions in order
        # to find the start and the end indices respectively.
        
        
        # We can set a mid pointer in order to divide the input
        # list into two parts, where the binary search occurs.
            # Run the main code:
        start = self.FindStart(nums, target)
        if start == -1:
            return [-1, -1]
        end = self.FindEnd(nums, target)
        if end == -1:
            return [-1, -1]
        return [start, end]
        
    def FindStart(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end: # not reversible
            mid  = int((end - start)/ 2) + start
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target: 
            return start
        elif nums[end] == target: 
            return end
        else:
            return -1
        
    def FindEnd(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end: # not reversible
            mid  = int((end - start)/ 2) + start
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target: 
            return end
        elif nums[start] == target: 
            return start
        else:
            return -1
        
        

        