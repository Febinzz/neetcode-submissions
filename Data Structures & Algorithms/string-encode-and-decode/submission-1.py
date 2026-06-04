class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
           # x=len(i)
            s=s+"%%"
            #s=s+str(x)
            s=s+i
        return s

    def decode(self, s: str) -> List[str]:
        a=[]
        a=s.split("%%")
        a.pop(0)
        return a

