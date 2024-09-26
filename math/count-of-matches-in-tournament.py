class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = []
        m = 0

        while n != 1:
            if n % 2 == 0:
                m = n / 2
                n = n - m
                matches.append(m)
            else:
                m = (n - 1) / 2
                n = n - m
                matches.append(m)

        return int(sum(matches))