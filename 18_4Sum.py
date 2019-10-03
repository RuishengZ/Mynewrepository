class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Exclude the extreme cases:
        if not nums or len(nums) < 4:
            return []
        
        # Initialize the result vector and reorder the num list
        solution = []
        nums.sort()
        
        # Combination process: 1 sum + 3 sum
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                remain = target - nums[i]
                ThreeSums = self.threeSumCombine(nums[i+1:], remain)
                for combine in ThreeSums:
                    solution.append([nums[i]] + combine)
                    
        return solution
    
    
    def threeSumCombine(self, GivenList, target):
        
        result = []
        
        # Exclude the extreme cases and avoid duplicates
        if len(GivenList) < 3:
            return []
        
        for i in range(len(GivenList) - 2):
            if i == 0 or GivenList[i] > GivenList[i - 1]:
                left = i + 1
                right = len(GivenList) - 1
                while left < right:
                    if GivenList[left] + GivenList[right] + GivenList[i] == target:
                        result.append([GivenList[i], GivenList[left], GivenList[right]])
                        left += 1
                        right -= 1
                        while left < right and GivenList[left] == GivenList[left - 1]:
                            left += 1
                        while left < right and GivenList[right] == GivenList[right + 1]:
                            right -= 1
                    
                    elif GivenList[left] + GivenList[right] + GivenList[i] > target:
                        while left < right:
                            right -= 1
                            if GivenList[right] < GivenList[right + 1]:
                                break
                    
                    else:
                        while left < right:
                            left += 1
                            if GivenList[left] > GivenList[left - 1]:
                                break
        return result