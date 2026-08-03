class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a=set(tasks)
        b=[]
        for i in a:
            x=tasks.count(i)
            b.append(x)
        ans2=max(b)
        ans=b.count(ans2)
        return (max(len(tasks),(((ans2-1)*(n+1))+ans)))

        
        