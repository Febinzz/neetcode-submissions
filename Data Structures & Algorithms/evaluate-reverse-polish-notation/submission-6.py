class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for i in tokens:
            if i== '+':
                x=a.pop()
                y=a.pop()
                ans=x+y
                print(ans)
                a.append(ans)
            elif i=='-':
                x=a.pop()
                y=a.pop()
                ans=y-x
                print(ans)
                a.append(ans)
            elif i=='*':
                x=a.pop()
                y=a.pop()
                ans=x*y
                print(ans)
                a.append(ans)
            elif i =="/":
                x=a.pop()
                y=a.pop()
                print(x,y)
                ans=int(y/x)
                print(ans)
                a.append(ans)
            else:
                a.append(int(i))
            print(a)
        return a[0]

        