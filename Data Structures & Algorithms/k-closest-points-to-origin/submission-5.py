class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        b=[]
        for i in range(0,len(points)):
            x=points[i][0]**2 + points[i][1]**2
            a.append([i,x])
        b=a.copy()
        a.sort(key=lambda x:x[1])
        c=[]
        print(a)
        d=[]
        for i in range(0,k):
            c.append(a[i][1])
        for i in range(0,len(b)):
            if b[i][1] in c:
                d.append(points[i])
        return d

        


       

      

        



        