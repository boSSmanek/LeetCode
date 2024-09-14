class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        f = edges[0]
        s = edges[1]

        if f[0] == s[0] or f[0] == s[1]:
            return f[0]
        
        return f[1]