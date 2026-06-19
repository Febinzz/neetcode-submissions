class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[]
        for i in range(0,len(prices)):
            for j in range(0,i+1):
                a.append(prices[i]-prices[j])
        return(max(a))



        