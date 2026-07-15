class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return i

        