class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    a.append(i+1)
                    a.append(j+1)
                    return a
        
        
        