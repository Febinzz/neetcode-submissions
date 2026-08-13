class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        if s[len(s)-1]==" ":
            for i in range(len(s)-1,-1,-1):
                if s[i]!=" ":
                    break
                else:
                    continue
            for j in range(i,-1,-1):
                if s[j]!=" ":
                    count=count+1
                else:
                    break
        else:
            for i in range(len(s)-1,-1,-1):
                if s[i]!=" ":
                    count=count+1
                else:
                    break
        return count
        