from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table_s, table_t = {}, {}       
        for i in range(len(s)):
            table_s.setdefault(s[i], 0)
            table_s[s[i]] += 1
            table_t.setdefault(t[i], 0)
            table_t[t[i]] += 1
        return table_t == table_s

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        skip = []
        for i in range(len(strs)):
            if i not in skip: 
                ans.append([strs[i]])
            for j in range(i+1, len(strs)):
                if j not in skip: 
                    if self.isAnagram(strs[i], strs[j]):
                        ans[-1].append(strs[j]) 
                        skip.append(j)
        return ans

strs = ["act","pots","tops","cat","stop","hat"]
s = Solution()
print(s.groupAnagrams(strs))

