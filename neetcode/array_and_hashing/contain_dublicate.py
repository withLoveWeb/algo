from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            check_var = nums[i] 
            for j in range(i+1, len(nums)):
                if check_var == nums[j]:
                    return True
        return False 


nums = []
s = Solution()
print(s.hasDuplicate(nums))
