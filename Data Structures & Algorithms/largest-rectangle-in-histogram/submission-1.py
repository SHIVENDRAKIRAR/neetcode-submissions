class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            mini = heights[i]
            for j in range(i,n):
                mini = min(heights[j] , mini)
                # if mini == 0:
                #     break
                ans = max(ans , mini*(j-i+1))
        return ans


        