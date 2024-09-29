from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i


nums = [3,4,5,6]
target = 7
s = Solution()
print(s.twoSum(nums, target))
