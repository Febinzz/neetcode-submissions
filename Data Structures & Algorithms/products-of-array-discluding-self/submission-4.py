from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the output array with 1s
        res = [1] * n
        
        # Pass 1: Compute the prefix products (left side)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Compute the postfix products (right side) and combine
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res


        