class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = []
        for i in s:
            if i not in a:
                a.append(i)
        l = 0
        r = 0

        b = []
        c = []

        while r < len(s):
            x = s[l:r + 1]

            for i in a:
                ans = x.count(i)
                c.append(ans)

            if (r - l + 1) - max(c) > k:
                l = l + 1
            else:
                b.append(len(x))

            r = r + 1
            c = []

        return(max(b))