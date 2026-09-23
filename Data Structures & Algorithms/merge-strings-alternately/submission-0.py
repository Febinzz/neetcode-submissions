class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        le=min(len(word1),len(word2))
        for i in range(0,le):
            s=s+word1[i]
            s=s+word2[i]
        if len(word1)>le:
            s=s+word1[le:len(word1)]
        if len(word2)>le:
            s=s+word2[le:len(word2)]
        return s


        