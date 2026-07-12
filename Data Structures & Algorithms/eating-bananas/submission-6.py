class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k=0
        l=0
        m=0
        b=[]
        a=[]
        left=1
        right=max(piles)
        while(left<=right):
            mid=(left+right)//2
            for i in range(0,len(piles)):
                k=piles[i]%mid
                if k==0:
                    l=0
                else:
                    l=abs(k-mid)
                m=piles[i]+l
                b.append(m//mid)
            if sum(b)<=h:
                a.append(mid)
                right=mid-1
            else:
                left=mid+1
            b=[]
            print(a)
            a.sort()
        return a[0]