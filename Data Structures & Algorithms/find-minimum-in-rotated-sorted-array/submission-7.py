class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        for i in range(0,len(nums)):
            if nums[i+1]<nums[i]:
                break
        return(nums[i+1])

        