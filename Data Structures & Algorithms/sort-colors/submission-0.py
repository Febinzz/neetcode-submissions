class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        for i in nums:
            a.append(i)
        a.sort()
        for i in range(0,len(a)):
            nums[i]=a[i]
        