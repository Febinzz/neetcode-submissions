class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lit=0
        for i in range(0,len(heights)-1):
            for j in range(len(heights)-1,i,-1):
                area=(j-i)*min(heights[i],heights[j])
                if(area>lit):
                    lit=area
        return lit