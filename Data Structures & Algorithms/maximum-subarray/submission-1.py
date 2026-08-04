class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        first=nums[0]
        second=nums[0]
        for i in range(1,len(nums)):
            first=max(nums[i],first+nums[i])
            second=max(first,second)
        return second



        