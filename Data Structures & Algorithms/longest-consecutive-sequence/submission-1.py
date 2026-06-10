class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        s=[]
        a=[]
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                continue  
            if nums[i]+1==nums[i+1]:
                count=count+1
            else:
                s.append(count)
                count=1
        s.append(count)
        return(max(s))


        