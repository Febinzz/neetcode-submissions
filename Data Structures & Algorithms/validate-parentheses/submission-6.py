class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i  in "({[":
                a.append(i)
            elif i ==")":
                if len(a)!=0 and a[-1]=="(":
                    a.pop()
                    continue
                else:
                    return False
            elif i =="}":
                if len(a)!=0 and a[-1]=="{" :
                    a.pop()
                    continue
                else:
                    return False
            else:
                if len(a)!=0 and a[-1]=="[": 
                    a.pop()
                    continue
                else:
                    return False
        if(len(a)==0):
            return True
        else:
            return False            
        