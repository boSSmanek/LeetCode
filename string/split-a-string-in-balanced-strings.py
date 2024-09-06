class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = prefix = 0

        for ch in s:
            if ch == 'R':
                prefix += 1
            else:
                prefix -= 1
            if not prefix:
                result += 1
        return result