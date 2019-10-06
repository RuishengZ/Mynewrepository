class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        quo = 0
        q = 1 # A temporary parameter to store the current quotinent
        r = dividend # A temporary parameter to store current dividend
        
        s1 = self.sign(dividend)
        s2 = self.sign(divisor)
        
        # Exclude some extreme cases:
        if divisor == 1:
            if s1 > 0:
                return min(2**31 - 1, dividend)
            else:
                return max(-2**31, dividend)
        
        if divisor == -1:
            if s1 > 0:   
                return max(-2**31, -dividend)
            else:
                return min(2**31 - 1, -dividend)
        
        
        # Normal cases:
        if s1 == s2:
            while q:
                q, r = self.shift_method(abs(r), abs(divisor))
                quo += q
            return quo
                    
        else:
            while q:
                q, r = self.shift_method(abs(r), abs(divisor))
                quo += q                  
            return -quo
        
################################# functions
    
    def sign(self, x):
        if x > 0:
            return 1
        else:
            return -1
        
    def shift_method(self, c_dividend, divisor):
        
        scale = 1
        
        if c_dividend < divisor:
            return 0,0
        
        else:
            while c_dividend > divisor:
                divisor <<= 1
                scale <<= 1
            
            if c_dividend == divisor:
                return scale, 0
            
            else:
                divisor >>= 1
                scale >>= 1
            return scale, c_dividend - divisor 
                