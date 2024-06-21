# Find All Numbers Disappeared in an Array


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = sorted(set(nums))
        tmp = nums[0]
        i = 0
        ans = []
        while tmp != nums[-1]:
            if num
        # for i in range(len(nums)):
        #     if tmp == nums[i]:
        #         tmp += 1
        #     else:
        #         ans.append(tmp)
        #         if nums[i+1]
        #         tmp = nums[i]
        return ans
    
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

