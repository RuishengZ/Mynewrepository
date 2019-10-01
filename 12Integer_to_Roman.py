class Solution:
    def intToRoman(self, num: int) -> str:
        
        Sym_map = {'1': 'I', '4': 'IV', '5': 'V', '9': 'IX', '10': 'X', '40': 'XL', '50': 'L', '90': 'XC', '100': 'C', '400': 'CD', '500': 'D', '900': 'CM', '1000': 'M'}
        
        # Get the number of digits of the input
        L = len(str(num))
        
        # Initialize the result paramenters
        rest_num = num
        result_l = []
        result_s = ''
        
        # Transformation
        for i in range(L - 1, -1, -1):
            cur_dig = rest_num // 10**i
            rest_num = rest_num % 10**i
            result_l.append(cur_dig)
        
        for j in range(len(result_l)):
            if result_l[j] <= 4:
                if result_l[j] < 4:
                    result_s += result_l[j]*Sym_map.get(str(10**(L - 1 - j)))
                else:
                    result_s += Sym_map.get(str(result_l[j]*10**(L - 1 - j)))

            elif result_l[j] == 9 or result_l[j] == 5:
                if 10**(L - 1 - j) < 1000:
                    result_s += Sym_map.get(str(result_l[j]*10**(L - 1 - j)))
                else:
                    result_s += result_l[j]*Sym_map.get(str(10**(L - 1 - j)))

            elif result_l[j] > 4 and result_l[j] < 9:
                result_s += Sym_map.get(str(5*10**(L - 1 - j)))
                result_s += (result_l[j] - 5)*Sym_map.get(str(10**(L - 1 - j)))
                    
        return result_s
                    
        
            
            
        