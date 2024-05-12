import json
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        zigzag = [[] for i in range(numRows)]
        counter = 0
        reverse = False
        for i in range(len(s)):

            tmp_counter = numRows - 2 - counter

            if counter == numRows-1:
                reverse = True
            elif counter == 0:
                reverse = False

            if reverse:
                if counter == numRows-1:
                    zigzag[counter].append(s[i])
                    for ii in range(numRows-2):
                        zigzag[counter].append(" ") 
                else:
                    for ii in range(numRows-2):
                        if tmp_counter == ii:
                            zigzag[counter].append(s[i])
                        else:
                            zigzag[counter].append(" ") 
                counter -= 1
            else:
                if counter == 0:
                    zigzag[counter].append(s[i])
                    for ii in range(numRows-2):
                        zigzag[counter].append(" ") 
                else: zigzag[counter].append(s[i])
                counter += 1
        
        
        # return
        for i in zigzag:
            print(i)



S = Solution()
# S.convert('PAYPALISHIRING',3)
S.convert('PAYPALISHIRING',4)