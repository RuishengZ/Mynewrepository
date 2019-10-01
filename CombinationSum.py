class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
    # Exclude the extreme case
        if not candidates:
            return [[]]
        
        # Initialize the final solution and partial solution
        result = []
        feasible = []
        
        # Rearrange the candidate list
        candidates.sort()
        
        Combination(result, candidates, target, feasible, 0)
        return result
            
# DFS function
def Combination(result, candidate, target, feasible, start):

    if target == 0:
        result.append(feasible[:])
        return

    for i in range(start, len(candidate)):
        if candidate[i] > target:
            return
        feasible.append(candidate[i])
        Combination(result, candidate, target - candidate[i], feasible, i)
        feasible.pop()

    return 
        
                
                
            