from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        start = 0
        while True:
            tmp = 0
            for i in range(start, len(nums)):
                tmp += nums[i]
                if tmp % k == 0:
                    result += 1
            if start + 1 == len(nums):
                break
            start += 1
        return result


s = Solution()
print(s.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))