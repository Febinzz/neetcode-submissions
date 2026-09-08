class Solution:
    def validPalindrome(self, s: str) -> bool:
        count=0
        x=s[::-1]
        if s==x:
            return True
        else:
            x=list(s)
            for i in range(0,len(s)):
                s=x.copy()
                s.pop(i)
                if s==s[::-1]:
                    return True
            return False


           
        