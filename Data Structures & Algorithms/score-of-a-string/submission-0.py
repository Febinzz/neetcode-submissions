class Solution:
    def scoreOfString(self, s: str) -> int:
        j=ord(s[0])
        print(j)
        ss=0
        for i in range(0,len(s)-1):
            ss=ss+abs(ord(s[i])-ord(s[i+1]))
        return(ss)
