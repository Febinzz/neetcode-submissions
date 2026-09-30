class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=[]
        count=0
        i=0
        while(i<len(nums)):
            if nums[i] not in a:
                count=count+1
                a.append(nums[i])
                i=i+1
            else:
                nums.pop(i)
            print(nums)
            print(a)
        return (count)




        