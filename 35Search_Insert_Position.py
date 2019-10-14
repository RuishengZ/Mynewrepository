class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # This is a typical binary searching problem, each of the 
        # binary branch represents one part of the list.
        
        # Starting with eliminate extreme cases:
        if not nums or len(nums) == 0:
            return 0
        
        # For normal cases, we use binary searching. Therefore
        # two pointers should be set for dividing the given list
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = int((end - start) / 2 + start)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
                
        # In the end, there will be three cases. The target value
        # may exist in the list like: [target___target___target].
        # Therefore, one could write:
        if target <= nums[start]:
            return start
        elif target <= nums[end]:
            return end
        else:
            return end + 1
                
        
        
        
                
        