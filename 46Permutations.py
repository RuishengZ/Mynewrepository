class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # We still use backtracking method
        
        # Firstly, we eliminate some extreme cases:
        if not nums or len(nums) == 0:
            return []
        
        # For the normal cases, we use backtracking method like we did
        # in the problem "Permutations II" (I actually solve that one before
        # solving this one). Some details of this method may be different 
        # here compared with "Permutations II" since there is no duplicates
        # in the given list. I think such differences would show in judgement
        # conditions.
        
        curlist = []
        result = []
        used = [0 for i in range(len(nums))]
        self.Solver(nums, result, curlist, used)
        return result
        
    def Solver(self, nums, result, curlist, used):
        if len(curlist) == len(nums):
            result.append(curlist[:])
            
        for i in range(len(nums)):
            if used[i]: continue
            # The judgement conditions here are simpler than them in "Permutation II"
            # because there is no repeated elements in the given nums list, so we don't
            # need to consider (nums[i] == nums[i - 1] and !used[i - 1])? This condition
            # is used to block the rest of those repeated elements and use only the first
            # one of them.
                
            used[i] = True
            curlist.append(nums[i])
            self.Solver(nums, result, curlist, used)
            used[i] = False
            curlist.pop()
                
        
                