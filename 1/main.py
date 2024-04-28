from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for a in range(i+1, len(nums)):
                if nums[i]+nums[a]==target:
                    return [i,a]

        
    


s = Solution()

nums = [3, 3]
target = 6

pr=s.twoSum(nums, target)
print(pr)