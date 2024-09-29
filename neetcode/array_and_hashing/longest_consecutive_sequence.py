class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        ans = 1
        sequence = []
        for n in nums:
            if ((n-1 in nums) ^ (n+1 in nums)):
                sequence.append(n)
        sequence = sorted(sequence)
        for i in range(0, len(sequence), 2):
            if ans < (sequence[i+1] - sequence[i] + 1):
                ans = sequence[i+1] - sequence[i] + 1
        return ans
        
