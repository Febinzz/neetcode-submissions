class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        a=[]
        for i in range(0,len(heights)):
            t=i-1
            k=0
            l=0
            u=i+1
            while(t>=0):
                if heights[t]>=heights[i]:
                    k=k+1
                    t=t-1
                    continue
                else:
                    break
            while(u<len(heights)):
                if heights[u]>=heights[i]:
                    l=l+1
                    u=u+1
                else:
                    break
            ans=(l+k+1)*heights[i]
            print(heights[i])
            print(l+k+1)
            print("ans:",ans)
            a.append(ans)
            ans=0       
        return(max(a))  
        