class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')', ']', '}']:
                if stack == []:
                    return False
                elif ((c == ')' and stack[-1] != '(') or 
                      (c == ']' and stack[-1] != '[') or
                      (c == '}' and stack[-1] != '{')):
                    return False
                stack.pop()
        if stack:
            return False
        else: 
            return True

