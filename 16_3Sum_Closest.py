class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # This problem is very similar to the ThreeSum problem before
        # but has a little bit difference.
        
        # We give an arbitrary initial value to the final output result at the 
        # beginning. It may be replaced by the optimal one later
        result = nums[0] + nums[len(nums) - 1] + nums[len(nums) - 2]
        
        # The search begins
        # len(nums) - 2 because we will have 3 pointers: i, start, end
        # the sum will be three indexed integer in nums by using these
        # three indices. Btw, sorting the given nums is necessary
        nums.sort()
        for i in range(len(nums) - 2):
            start = i + 1
            end  = len(nums) - 1
            temp_sum = 0
            while start < end:
                temp_sum = nums[i] + nums[start] + nums[end]
                if temp_sum > target:
                    end -= 1
                else:
                    start += 1
                    
                # Judge if the current solution should be replaced or not    
                if abs(temp_sum - target) < abs(result - target):
                    result = temp_sum
                    
        return result
                    
                    