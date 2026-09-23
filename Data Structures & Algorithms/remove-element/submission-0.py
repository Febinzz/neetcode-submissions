class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        while(i<len(nums)):
            if nums[i]==val:
                nums.pop(i)
            else:
                k=k+1
                i=i+1
        print(k)
        print(nums)
        nums.sort()
        return k
            