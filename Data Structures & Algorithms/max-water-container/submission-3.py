class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        lit = (r-l) * min(heights[r], heights[l])
        while (l < r):
            area=(r-l) * min(heights[r], heights[l])
            if area>lit:
                lit=area
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return lit