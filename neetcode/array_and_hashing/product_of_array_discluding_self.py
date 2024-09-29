class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for elem in nums:
            product *= elem
            if elem == 0:
                zero += 1
        
        if zero <= 1:
            ans = [product] * len(nums)
        else:
            return [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                ans[i] = ans[i] // nums[i]
            else:
                ans[i] = 1
                for j in range(len(nums)):
                    if i != j and nums[j] != 0:
                        ans[i] *= nums[j]

        return ans
