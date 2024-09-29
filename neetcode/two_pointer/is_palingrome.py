import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.translate(str.maketrans('', '', string.punctuation + ' '))
        left = 0
        right = -1 

        for i in range(len(s)//2):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


    
var = 'abb'
s = Solution()
print(s.isPalindrome(var))
