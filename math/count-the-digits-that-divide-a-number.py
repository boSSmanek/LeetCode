class Solution:
    def countDigits(self, num: int) -> int:
        result = 0

        for i in str(num):
            if int(num) % int(i) == 0:
                result += 1
        
        return result