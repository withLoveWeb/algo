class Solution:
    def intToRoman(self, num: int) -> str:
        rome = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        rome_num = "" 
        while True:
            if num // rome["M"] > 0: # 10000
                rome_num += "M"*(num // rome["M"])
                num = num % rome["M"]
                continue
            if num // rome["C"] > 0: # 1000
                digit = num // rome["C"]
                if digit == 9:       # 900
                    rome_num += "CM"
                    num = num % rome["C"]
                    continue
                if digit == 4:      # 400
                    rome_num += "CD"
                    num = num % rome["C"]
                    continue
                if digit >= 5:
                    rome_num += "D"
                    num -= rome["D"]
                    continue
                rome_num += "C"
                num -= rome["C"]
                continue
            if num // rome["X"] > 0: # 100
                digit = num // rome["X"]
                if digit == 9:       # 90
                    rome_num += "XC"
                    num = num % rome["X"]
                    continue
                if digit == 4:      # 40
                    rome_num += "XL"
                    num = num % rome["X"]
                    continue
                if digit >= 5:
                    rome_num += "L"
                    num -= rome["L"]
                    continue
                rome_num += "X"
                num -= rome["X"]
                continue
            if num > 0:             # 10
                digit = num
                if digit == 9:      # 9
                    rome_num += "IX"
                    num = num // rome["X"]
                    continue 
                if digit == 4:      # 4
                    rome_num += "IV"
                    num = num // rome["X"]
                    continue
                if digit >= 5:
                    rome_num += "V"
                    num -= rome["V"]
                    continue
                rome_num += "I"
                num -= rome["I"]
                continue
            return rome_num
        
        




sol = Solution()
print(sol.intToRoman(3749))



class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hrns = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ths  = ["","M","MM","MMM"]
        
        return ths[num/1000] + hrns[(num%1000)/100] + tens[(num%100)/10] + ones[num%10]
    



class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman
