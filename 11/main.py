from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        square = 0
        left = 0
        right = len(height) - 1
        while left < right:
            pre_square = (right-left)*min(height[left],height[right])
            square = max(square,pre_square)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return square
            


height = [2,3,4,5,18,17,6]
test = Solution()
print(test.maxArea(height))