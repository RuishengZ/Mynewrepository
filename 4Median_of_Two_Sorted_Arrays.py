class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Since the run time complexity should be O(log (m+n)), so it means
        # Binary search method should be used here.
        
        # For even number case
        #              L1   R1
        # e.g: num1 : 3 5 | 8 9         cut1: how many numbers are before the cut boundary
        #      num2 : 1 2 7 | 10 11 12  cut2: how many numbers are before the cut boundary
        #                 L2  R2
        
        # Then we can create the third number vector num3:
        # num3 : 1 2 3 5 7 | 8 9 10 11 12
        # One could see that the way of we cut the vector num2 can be known if we knew the
        # length of num3 and how we cut the vector num1. This means we could get the 
        # final result by only doing opperations on 1 vector, which implies that the
        # run time complexity of our method will be O(log(min(m,n))).
        
        # So the median will exactly be either the element at the middle index (odd case)
        # or the average of sum of the first number before boundary and the first number
        # after the boundary (even case)
        
        # The acceptable cut case (may not the final cut case) should satisfy the
        # following conditions:
        # (1) L1 < R2
        # (2) L2 < R1
        # Therefore, if L1 > R2: then cut1 must be moved 1 step left
        # Similarly, if L2 > R1: then cut1 must be moved 1 step right
        
        # For convenience purpose, we always name the shorter one of the two
        # given vectors as "num1"
        
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        len3 = len(nums1) + len(nums2)
        cut1 = 0
        cut2 = 0
        
        # The following two variables are used for applying binary search
        # on nums1
        cutL = 0
        cutR = len(nums1)
        
        # Define some temporary variables used in the following binary searching
        L1 = 0
        L2 = 0
        R1 = 0
        R2 = 0
        
        while cut1 <= len(nums1): 
            # Unlike the binary search method before, we
            # don't use e.g. left < right here because one could meet the
            # situation e.g. sometimes we have: nums1: 3 4 5 6 |. And if 
            # for example: nums1 doesn't need to be cut or it needs to be 
            # cut completely, then we assign it the 
            
            cut1 = (cutR - cutL) + cutL
            cut2 = (len3 // 2) - cut1
            
            # If the nums1 or nums2 do not need to be cut or all the 
            # elements of them need to be cut, e.g.: | 3 4 5 6 or
            # 3 4 5 6 |. Then we need to assign an extremely large/small 
            # value to fill L1/L2 and R1/R2 parts.
            if cut1 == 0:
                L1 = float('-inf')
            else:
                L1 = nums1[cut1 - 1]
                
            if cut2 == 0:
                L2 = float('-inf')
            else:
                L2 = nums2[cut2 - 1]
                
            if cut1 == len(nums1):
                R1 = float('inf')
            else:
                R1 = nums1[cut1]
                
            if cut2 == len(nums2):
                R2 = float('inf')
            else:
                R2 = nums2[cut2]
            
            # Judging if the it satisfies the median conditions:
            # If violated:
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            
            # If it's acceptable:
            else:
                if len3 % 2 == 0: #(for even number case)
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1 + R1) / 2
                else:
                    R1 = min(R1, R2)
                    return R1
        return -1
            