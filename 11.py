from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        square = 0
        left = 0
        right = len(height) - 1
        while left < right:
            square = max(square,(right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return square
            


height = [2,3,4,5,18,17,6]
test = Solution()
print(test.maxArea(height))


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
