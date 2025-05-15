# [9] Palindrome Number

# O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        temp = ""
        for i in range(len(str_x)-1, -1, -1):
            temp += str_x[i]
        return str_x == temp

# O(n/2)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        n = len(str_x)
        for i in range(n//2):
            if str_x[i] != str_x[-(i+1)]:
                return False
        return True
