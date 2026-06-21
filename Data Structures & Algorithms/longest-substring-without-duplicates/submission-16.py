class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        b=0
        flag=0
        if len(s)==0:
            return 0
        if(s.isspace()):
            return 1
        for i in range(0,len(s)):
            a=[]
            a.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in a:
                    a.append(s[j])
                else:
                    if(len(a)>b):
                        b=len(a)
                        flag=1
                    break    
            if(len(a)>=b):
                b=len(a)
        if flag==1:
            return b
        else:
           return(len(s))

        