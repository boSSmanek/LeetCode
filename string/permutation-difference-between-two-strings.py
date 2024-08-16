class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = sum(abs(i - t.index(s[i])) for i in range(len(s)) if s[i] != t[i])
        return result