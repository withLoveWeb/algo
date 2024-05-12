class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        end = 1
        len_substr = 0
        if len(s) <= 1:
            return len(s)
        while True:

            if len(s[start:end]) == len(set(s[start:end])):
                end +=1
            else:
                start +=1
            if len_substr < end - start - 1:
                len_substr = end - start - 1
            # if len(s)-start <= len_substr:
            #     if len_substr == 0:
            #         return len(s)
            #     return len_substr
            if end > len(s):
                if len_substr == 0:
                    return len(s)
                return len_substr
            

s = Solution()
print(s.lengthOfLongestSubstring("aab"))