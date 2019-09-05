class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.alllist = []
        self.candiList = []
        self.nowValue = 0
        candidates.sort()
        
        self.Numbplus(self.nowValue, target, candidates, self.candiList, self.alllist)
        return self.alllist
    
    
    def Numbplus(self, current_value, target, GivenList, candiList, allList):
        for i in GivenList:
            current_value += i
            if current_value < target:
                candiList.append(i)
                allList, candiList, current_value = self.Numbplus(current_value, target, GivenList, candiList, allList)
                candiList = candiList[:-1]
                current_value -= i
                
            
            elif current_value == target:
                compareList = candiList.copy()
                candiList.append(i)
                compareList.append(i)
                compareList.sort()
                if compareList not in allList:
                    allList.append(candiList)
                candiList = candiList[:-1]
                current_value -= i
                break
                
            elif current_value > target:
                current_value -= i
                break
                
        
        return allList, candiList, current_value
                
                
                
            
