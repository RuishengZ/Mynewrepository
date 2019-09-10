class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Initialize parameters
        dcounter = 0
        dnumb = 0
        current = nums[0]
        
        # Replace the duplicates which appear more than twice
        for i in range(len(nums)):
            if nums[i] == current:
                dcounter += 1
                if dcounter > 2:
                    dnumb += 1
                    nums.remove(nums[i])
                    nums.insert(i, '0')
            else:
                current = nums[i]
                dcounter = 1
        
        # Reorder list        
        for i in range(len(nums)):
            if nums[i] == '0':
                nums.append(nums.pop(nums.index(nums[i])))
        return len(nums) - dnumb