class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev_num = 0
        t = x

        while t != 0:
            d = t % 10
            rev_num = rev_num * 10 + d
            t //= 10
        
        return rev_num == x