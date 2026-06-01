class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        b=[]
        for i in range(len(strs)):
            a=[]
            for j in range(len(strs)):
                 if ''.join(sorted(strs[i]))== ''.join(sorted(strs[j])):
                    a.append(strs[j])
            if a not in b:
                b.append(a)
        return b
