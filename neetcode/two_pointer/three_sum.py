from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        ans = []
        for i, n in enumerate(nums): 
            if n <= 0 and len(nums[i:]) >= 3:
                tmp = self.twoSum(nums[i+1:],-n if n else 0)
                if tmp is not None:
                    for l in tmp:
                        l.append(n)
                        if l not in ans:
                            ans += tmp
            else:
                return ans 

    def twoSum(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        ans = []
        while r > l:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] == target:
                if [nums[l], nums[r]] not in ans:
                    ans.append([nums[l], nums[r]])
                r -= 1
                l += 1
        return ans


s = Solution()
nums=[-2,0,0,2,2]
print(s.threeSum(nums))
