class MyHashMap:
    def __init__(self):
        self.res=[]
    def put(self, key: int, value: int) -> None:
        print(self.res)
        flag=0
        a=[]
        a.append(key)
        a.append(value)
        for i in range(0,len(self.res)):
            if self.res[i][0]==key:
                self.res[i][1]=value
                flag=1
        if flag==0:
            self.res.append(a)
        a=[]
    def get(self, key: int) -> int:
        print(self.res)
        for i in range(0,len(self.res)):
            if self.res[i][0]==key:
                return self.res[i][1]
        return -1
    def remove(self, key: int) -> None:
        print(self.res)
        i=0
        while(i<len(self.res)):
            if self.res[i][0]==key:
                self.res.pop(i)
            else:
                i=i+1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)