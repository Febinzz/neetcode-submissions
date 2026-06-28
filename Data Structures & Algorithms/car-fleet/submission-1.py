class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        b=sorted(zip(position,speed))
        print(b)
        a=[]
        t=0
        c=[]
        for i in range(len(position)):
            t=(target-b[i][0])/b[i][1]
            a.append(t)
            t=0
        c.append(a[len(a)-1])
        for i in range(len(a)-2,-1,-1):
            if a[i]<=c[-1]:
                continue
            else:
                c.append(a[i])
        print(c)
        return(len(c))



