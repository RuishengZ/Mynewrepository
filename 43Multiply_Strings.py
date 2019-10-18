class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # Eliminate the extreme cases:
        if len(num1) == 0 or len(num2) == 0:
            return '0'
        
        # As for the normal multiplication cases like:
        #                          3 3
        #                          3 6
        #                     ___________
        #                          1 8
        #                        1 8
        #                        0 9
        #                      0 9  
        #                  _______________
        #                      1 1 8 8
            
        # So the maximum length of 2 2-length integers production will be 4
        # The positions where the production of every two digits pair 
        # fall in are important we'll use the for loop indices i and j to describe
        # them
        digits = [0 for d in range(len(num1) + len(num2))]
        product = 0
        result = ''
        
        # These two parameters represent where the tens place and ones place
        # of every two digits product should fall in the final result
        p1 = 0
        p2 = 0
        
        # This temporary sum contains the current product of two digits 
        # as well as the carry
        temp_sum = 0
        
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                temp_sum  = product + digits[p2]
                digits[p1] += temp_sum // 10
                digits[p2] = temp_sum % 10
                
        for digit in digits:
            if not (digit == 0 and len(result) == 0):
                result += str(digit)
                
        if len(result) == 0:
            return '0'
        else:
            return result
            
                
                
                