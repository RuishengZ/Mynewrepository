class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Judge if there is no way to run clockwise direction
        if sum(gas) < sum(cost):
            return -1
        
        # Find the unique way of traveling
        station = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i] # The remaining gas after arriving next station
            if tank < 0:
                station = i + 1 # Maybe it's next station
                tank = 0
                
        return station