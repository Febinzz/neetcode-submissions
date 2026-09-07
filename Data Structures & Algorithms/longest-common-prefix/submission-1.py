class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0
        for i in range(len(strs[0]),-1,-1):
            x=strs[0][0:i] 
            print(x)
            for i in range(0,len(strs)):
                if x in strs[i]:
                    count=count+1
                else:
                    continue
            if count==len(strs):
                return x
            count=0
        return ""