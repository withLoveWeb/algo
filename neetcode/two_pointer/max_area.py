from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights)
        l, r = 0, len(heights) - 1
        ans = -1
        while r - l != 0:
            if ans < min(heights[l], heights[r]) * (r - l):
                ans = min(heights[l], heights[r]) * (r - l)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return ans

            

height = [1,7,2,5,4,7,3,6]
# height = [2,2,2]
s = Solution()
print(s.maxArea(height))
