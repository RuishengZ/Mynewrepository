class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
                
        
        n = nums.count(val) # Get the number of the element that to be deleted
        r = len(nums) - n # Return the length of the rest list
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums.remove(nums[i])
                nums.insert(i, '0')
                
        "Put all '0' in the end of the list"        
        for i in range(len(nums)):
            if nums[i] == '0':
                nums.append(nums.pop(nums.index(nums[i])))
        return r
        
                

        
        