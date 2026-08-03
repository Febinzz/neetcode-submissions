class MedianFinder:

    def __init__(self):
        self.k=[]
        

    def addNum(self, num: int) -> None:
        self.k.append(num)
        self.k.sort()

    def findMedian(self) -> float:
        if len(self.k)%2!=0:
            return self.k[len(self.k)//2]
        else:
            x=(self.k[len(self.k)//2]+ self.k[(len(self.k)//2)-1])/2
            return x
        
        