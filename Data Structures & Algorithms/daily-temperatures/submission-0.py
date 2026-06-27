class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(temperatures)):
            flag=0
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result.append(abs(j-i))
                    flag=1
                    break
            if flag==0:
                result.append(0)
        return result
                
        

        