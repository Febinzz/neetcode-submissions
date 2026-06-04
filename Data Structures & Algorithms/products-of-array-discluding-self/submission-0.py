import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        s=0
        for i in range(0,len(nums)):
            x=nums[i]
            nums[i]=1
            s=math.prod(nums)
            a.append(s)
            nums[i]=x
        return a


        