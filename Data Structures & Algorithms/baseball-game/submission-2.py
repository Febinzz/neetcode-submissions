class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        s=0
        for i in operations:
            if i=='D':
                x=int(a[-1])
                x=x*2
                a.append(x)
            elif i=='C':
                a.pop(-1)
            elif i=='+':
                x1=int(a[len(a)-1])
                x2=int(a[len(a)-2])
                x3=x1+x2
                a.append(x3)
            else:
                j=int(i)
                a.append(j)
        ans=sum(a)
        return(ans)
        