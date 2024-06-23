# Island Perimeter
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for j in range(len(grid)):
            print(grid[j])
            for i in range(len(grid[j])):
                if grid[j][i] == 1:
                    if j == 0:
                        p += 1
                    elif not grid[j-1][i]:
                        p += 1
                    if i == len(grid[j])-1:
                        p += 1
                    elif not grid[j][i+1]:
                        p += 1
                    if j == len(grid)-1:
                        p += 1
                    elif not grid[j+1][i]:
                        p += 1
                    if i == 0:
                        p += 1
                    elif not grid[j][i-1]:
                        p += 1
        return p

grid = [[]]
s = Solution()
print(s.islandPerimeter(grid))


