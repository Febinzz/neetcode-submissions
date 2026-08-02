class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            x=len(stones)-1
            stones.sort()
            if stones[x]== stones[x-1]:
                stones.pop()
                stones.pop()
            else:
                y=stones[x]-stones[x-1]
                stones.pop()
                stones[-1]=y
        if len(stones)==0:
            return 0
        else:
            return stones[0]
        