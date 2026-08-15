class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            s=""
            s=s+i[11]
            s=s+i[12]
            if (int(s)>60):
                count=count+1
        return count

        