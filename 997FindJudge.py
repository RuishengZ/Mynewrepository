class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        "Initialization"
        Man_list = range(1,N+1)
        judge_candi = 0 # The judge candidates
        
        
        for i in Man_list:
            judge_flag = 1   # The base requirement of being the judge
            trust_tickets = 0 # Indicate how many people trust the judge
            for j in trust:
                if j[0] == i:
                    judge_flag = 0
                    break
                if j[1] == i:
                    trust_tickets += 1
                    
            if judge_flag == 1 and trust_tickets == N - 1:
                judge_candi = i
                
        if judge_candi == 0:
            return -1
        else:
            return judge_candi
                
                    
            
        