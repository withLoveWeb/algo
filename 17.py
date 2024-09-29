from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]        
        ans = []
        pre_ans = []
        for i in range(len(digits)):
            pre_ans.append(letters[int(digits[i])])
        cancel = 1 if len(pre_ans) else 0
        for i in range(len(pre_ans)):
            cancel = cancel * len(pre_ans[i])
        j = 0
        while True:
            if j == cancel:
                return ans
            if len(pre_ans) >= 1:
                combination = pre_ans[0][j%len(pre_ans[0])]
            if len(pre_ans) >= 2:
                combination += pre_ans[1][(j%(len(pre_ans[0])*len(pre_ans[1])))//len(pre_ans[0])]
            if len(pre_ans) >= 3:
                combination += pre_ans[2][(j%(len(pre_ans[0])*len(pre_ans[1])*len(pre_ans[2])))//(len(pre_ans[0])*len(pre_ans[1]))]
            if len(pre_ans) >= 4:
                combination += pre_ans[3][(j%(len(pre_ans[0])*len(pre_ans[1])*len(pre_ans[2])*len(pre_ans[3])))//(len(pre_ans[1])*len(pre_ans[2])*len(pre_ans[0]))]
            ans.append(combination)
            j += 1
        
        
        
s = Solution()
print(s.letterCombinations("9387"))


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb): 
            if idx == len(digits):
                res.append(comb[:])
                return
            
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res
