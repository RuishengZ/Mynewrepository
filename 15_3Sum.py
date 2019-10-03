class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Exclude the extreme case
        if not nums or len(nums) < 3:
            return []
        
        # Initialize the parameters and reorder the given list: 
        solution = [] # Use it to store all sub-solutions 
        nums.sort()
        
        for i in range(len(nums) - 2):
        # -2 because of the extreme case where we only have 3 elements
        # since we have 3 pointers: i, left, right
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                
                while left < right: # not reversible
                    # a + b + c = 0 is equal to a + b = -c 
                    if nums[left] + nums[right] == -nums[i]:
                        solution.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Since there are some duplicates in the given list, we need to skip                           # them
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1

                    elif nums[left] + nums[right] > -nums[i]:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]:
                                break
                            
                    else:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]:
                                break
                    
        return solution
        
        
        

        
    
            
        