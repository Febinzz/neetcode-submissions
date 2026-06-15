class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.split())
        s=s.lower()
        k=len(s)-1
        x="qwertyuiopasdfghjklzxcvbnm1234567890"
        a=[]
        b=[]
        for i in s:
            if i in x:
                a.append(i)
            else:
                continue
        b=a[::-1]
        if a==b:
            return(True)
        else:
            return(False)