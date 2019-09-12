class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Approach 1 (Insert the element one by another)
        # r_ele = 0
        # for i in range(k):
        #     r_ele = nums.pop()
        #     nums.insert(0, r_ele)
        
        # Approach 2 (Cut the given list into slices)
        k  = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
                
            