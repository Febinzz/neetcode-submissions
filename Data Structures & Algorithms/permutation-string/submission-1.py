class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        while(r<len(s2)):
            x=s2[l:r+1]
            if sorted(x)==sorted(s1):
                return(True)
            else:
                l=l+1
                r=r+1
        return(False)