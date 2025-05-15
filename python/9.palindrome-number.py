# [9] Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        temp = ""
        for i in range(len(str_x)-1, -1, -1):
            temp += str_x[i]
        return str_x == temp