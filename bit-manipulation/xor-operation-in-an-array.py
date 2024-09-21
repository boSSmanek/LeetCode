class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = []
        for i in range(n):
            m = start + 2 * i
            r.append(m)
            
        x = 0
        for i in range(len(r)):
            x = x ^ r[i]
        return x