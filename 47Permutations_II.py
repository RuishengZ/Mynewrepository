class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # This problem is a typical backtracking problem, therefore
        # recursion is needed.
        
        # We first eliminate the extreme cases:
        if not nums or len(nums) == 0:
            return []
        
        # For the normal cases, we need to cancel out the duplicates 
        # combination sub-solutions, like what we did in the "Combination"
        # problem. For example, given the nums list: [1,1,2] if we do not
        # restrict the use of the identical elements, which are two "1" here,
        # then both "1" could generate the sub-solution [1,1,2] during the
        # backtracking process. Therefore, a list of boolean variables will 
        # be used here to avoid using the same element, and to use a judgement
        # condition nums[i] == nums[i - 1] to avoid using elements with the
        # same value.
                
        nums.sort()
        curlist = []
        result = []
        used = [0 for i in range(len(nums))]
        self.Solver(nums, curlist, result, used)
        return result
        
    def Solver(self, nums, curlist, result, boollist):
        if len(curlist) == len(nums):
            result.append(curlist[:])
            
        for i in range(len(nums)):
            if boollist[i] or (i > 0 and nums[i] == nums[i - 1] and not boollist[i - 1]):
                # Unlike in the combination problem, we additionally add 
                # "and not boollist[i - 1]" here in the judgment since every
                # element in the given list will be used and each element must 
                # be used no more than once. (In the combination problem, each element
                # can be used more than once, you just need to make sure there is no
                # duplicate in the final result) So the difference comes in here.
                continue
            boollist[i] = True
            curlist.append(nums[i])
            self.Solver(nums, curlist, result, boollist)
            boollist[i] = False
            curlist.pop()
            
            
            
    
            
        