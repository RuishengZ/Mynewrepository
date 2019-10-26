class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # This is a typical recursion problem, where the power value n is
        # divided by 2 continuously, the basic value remains unchanged
        
        # e.g 1: 2^2 = 2^1 * 2^1 = (2^0 * 2^0 * 2) * (2^0 * 2^0 * 2) = (1 * 1 * 2)
        # * (1 * 1 * 2) = 4
        
        # e.g 2: 2^3 = 2^1 * 2^1 * 2 = (2^0 * 2^0 * 2) * (2^0 * 2^0 * 2) * 2 = 8
        
        # We first separate the positive and negative cases:
        
        if n > 0:
            return self.Pow(x, n)
        else:
            return 1 / self.Pow(x, -n)
        
        
    def Pow(self, x, n):
        
        if n == 0:
            # The deepest stage of the recursion
            return 1
        
        temp = self.Pow(x, n//2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x
            
        
        
        