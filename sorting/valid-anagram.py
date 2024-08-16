class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash, tHash = {}, {}
        for i in range(len(s)):
            sHash[s[i]] = 1 + sHash.get(s[i], 0)
            tHash[t[i]] = 1 + tHash.get(t[i], 0)

        for h in sHash:
            if sHash[h] != tHash.get(h, 0):
                return False
        
        return True