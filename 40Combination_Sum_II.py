class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Eliminate the extreme cases:
        if not candidates or len(candidates) == 0:
            return []
        
        # For normal cases:
        candidates.sort()
        current_solution = []
        result = []
        self.CombinationF(candidates, target, current_solution, result, 0)
        return result
        
        
        
    def CombinationF(self, candidates, target, cs, result, start):
        if target < 0: return
        elif target == 0:
            result.append(cs[:])
            return result
            
        else:
            for i in range(start,len(candidates)):
                
                # The following if judgement step is aimed to avoid the duplicate
                # sub-solutions. For example the candidates list:[1,1,2,5,6,7,10]
                # and the target is 8, we start with taking the first element 1
                # and then we go into recursion. So we can get [1,1,6], [1,2,5] and
                # [1,7]. However, when the for loop index i of the most outside 
                # recursion move to the second element, that is also 1. If we 
                # run the recursion without eliminating this 1, we can get [1,2,5]
                # and [1,7] again, which are already existing in our result list.
                # Remember, we only use the recursion step-by-step, deeper and deeper 
                #to add new elements into our sub-solution, not any specific for loop 
                # in each recursion process, that means every index i in every for loop
                # only provides the start point of collecting sub-solutions.
                # 
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                    
                cs.append(candidates[i])
                self.CombinationF(candidates, target - candidates[i], cs, result, i + 1)
                cs.pop()
                
                
            
        