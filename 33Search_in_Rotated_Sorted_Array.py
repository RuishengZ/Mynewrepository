class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # This problem is a binary search problem since the 
        # time complexity is required to be (logn)
        # Binary searching here means to search two parts of the list
        # e.g: 4 5 6 7 (the first part)  0 1 2 3 (the second part)
        
        # Eliminate the extreme cases:
        if not nums or len(nums) == 0:
            return -1
        
        # Normal cases: binary searching:
        
        # Two pointers for set up the searching range
        start = 0
        end = len(nums) - 1
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        while start + 1 < end:
            mid = int((end - start) / 2) + start
            if nums[mid] == target:
                return mid
            
            if nums[start] < nums[mid]:
                # The first part
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
                
            else:
                # The second part
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
                    
        return -1
                
        