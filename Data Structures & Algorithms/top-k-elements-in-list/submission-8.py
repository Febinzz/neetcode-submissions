class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        for i in range(0,k):
            ma=0
            for j in nums:
                if(nums.count(j)>ma):
                    ma=nums.count(j)
                    maxx=j
            if maxx not in a:
                a.append(maxx)
                while maxx in nums:
                    nums.remove(maxx)
        return a  