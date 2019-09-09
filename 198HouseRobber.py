class Solution:
    def rob(self, nums: List[int]) -> int:
        "House robber or bank robber? I prefer bank robber."
        
        if len(nums) == 0:  # Considering that no bank is over there
            return 0
        elif len(nums) == 1: # Only one bank nearby
            return nums[0]
        elif len(nums) == 2: # Only two banks nearby
            return max(nums)
        elif len(nums) > 2: # More than two banks nearby (common situation)
            bank_idx = 2
            if nums[0] > nums[1]:
                nums[1] = nums[0]
            "Initialize parameters"
            while bank_idx <= len(nums) - 1:
                nums[bank_idx] = max(nums[bank_idx - 2] + nums[bank_idx], nums[bank_idx - 1])
                bank_idx += 1
                
        return nums[-1]

                        
                        
        
        
# Method 2:
#       else:
#             "Initialize parameters"
#             r_bank = 0  # The largest sum if you robbed this bank
#             nr_bank = 0 # The largest sum if you did not rob this bank
            
#             for bank in nums:
#                 temp = max(r_bank, nr_bank)
#                 r_bank = nr_bank + bank
#                 nr_bank = temp
                
#             return max(r_bank, nr_bank)
                      

                
            
