class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                flag=1
                break
            else:
                flag=0
        if flag==1:
            return True
        else:
            return False
            