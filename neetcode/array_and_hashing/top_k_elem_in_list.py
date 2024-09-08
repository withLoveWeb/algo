from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = {}
        for elem in nums:
            frequent_dict.setdefault(elem, 0)
            frequent_dict[elem] += 1
        frequent_dict = sorted(frequent_dict.items(), key=lambda key: key[1], reverse=True)
        return [item[0] for item in frequent_dict[:k]] 
        
s = Solution()
nums = [1,2,2,3,3,3,4]
k=2
print(s.topKFrequent(nums, k))
