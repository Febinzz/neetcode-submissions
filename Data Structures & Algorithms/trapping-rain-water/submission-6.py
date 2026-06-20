class Solution:
    def trap(self, height: List[int]) -> int:
        x = 0

        for i in range(len(height)):
            if height[i] != 0:
                x = i
                break

        z = []
        y = []
        ans = 0

        for i in range(x, len(height) - 1):
            z = height[:i]
            y = height[i+1:]
            if len(z)==0:
                z1=0
            else:
                z1 = max(z)
            y1 = max(y)

            area = min(z1, y1) - height[i]

            if area > 0:
                ans = ans + area

        return ans