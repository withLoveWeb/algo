import json
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zigzag = [[] for i in range(numRows)]
        counter = 0
        reverse = False
        
        for i in range(len(s)):
            zigzag[counter].append(s[i])

            if counter == numRows-1:
                reverse = True
            elif counter == 0:
                reverse = False

            
            if reverse: counter -= 1
            else: counter += 1
        
        output = ''
        for i in zigzag:
            output += ''.join(i)
        return output



S = Solution()
# S.convert('PAYPALISHIRING',3)
print(S.convert('ABC',2))