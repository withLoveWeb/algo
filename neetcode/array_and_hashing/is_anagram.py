


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



s = "jma"
t = "jam"
sol = Solution()
print(sol.isAnagram(s,t))
