# https://leetcode.com/problems/sqrtx/
# 2147483647

class Solution:
    def mySqrt(self, x: int) -> int:
        mid = 2147483647
        half_mid = mid // 2
        print(mid ** 0.5, half_mid ** 0.5 * 2 **0.5)

s = Solution()
s.mySqrt(12)