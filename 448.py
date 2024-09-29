# Find All Numbers Disappeared in an Array


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = sorted(set(nums))
        i = 0
        ans = []
        for tmp in range(1,n+1):
            try:
                if nums[i] == tmp:
                    i += 1
                else:
                    ans.append(tmp)
            except IndexError:
                ans.append(tmp)
        return ans
    
s = Solution()
print(s.findDisappearedNumbers([1,1,2]))

