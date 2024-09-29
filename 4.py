from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        merged_len = len(nums1)+len(nums2)
        a = 0
        b = 0
        for i in range(merged_len):
            if b >= len(nums2): 
                merged_list.append(nums1[a])
                a += 1
            elif a >= len(nums1): 
                merged_list.append(nums2[b])
                b += 1
            elif nums1[a] <= nums2[b]:
                merged_list.append(nums1[a])
                a += 1
            else:
                merged_list.append(nums2[b])
                b += 1
        if merged_len % 2 == 0:
            print(merged_list[int(merged_len/2-0.5)])
            return (merged_list[int(merged_len/2-0.5)] + merged_list[int(merged_len/2+0.5)])/2
        else: return merged_list[int(merged_len/2)]
        
        
        

S = Solution()

print(S.findMedianSortedArrays([1,2],[3,4]))