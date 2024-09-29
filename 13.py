class Solution:
    def romanToDigit(self, s, digit):
        if s:
            tmp_ans = []
            for val in digit:
                pattern = s[-len(val):]
                if pattern == val:
                    tmp_ans.append(val)
            if tmp_ans:
                longest_key = max(tmp_ans, key=len)
                s = s[:-len(longest_key)]
                ans = digit.index(longest_key)+1
            else:
                ans = 0
            return (s, ans)
        else:
            return (s,0)
    def romanToInt(self, s: str) -> int:
        ones = ["I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hrns = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ths  = ["M","MM","MMM"]
        ans = 0

        [s,digit] = self.romanToDigit(s, ones)
        ans += digit
        [s,digit] = self.romanToDigit(s, tens)
        ans += digit*10
        [s,digit] = self.romanToDigit(s, hrns)
        ans += digit*100
        [s,digit] = self.romanToDigit(s, ths)
        ans += digit*1000
        return ans


        



    


s = Solution()
print(s.romanToInt("MDLXX"))