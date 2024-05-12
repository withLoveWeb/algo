from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        square = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                pre_square = (j-i)*min(height[j],height[i])
                if square < pre_square:
                    square = pre_square
        return square


height = [1,1]
test = Solution()
test.maxArea(height)