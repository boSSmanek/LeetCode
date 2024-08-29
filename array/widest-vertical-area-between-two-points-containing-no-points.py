class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s = []
        for i in range(len(points)):
            s.append(points[i][0])
        
        s.sort()

        res = 0
        for i in range(len(s) - 1, 0, -1):
            d = s[i] - s[ i - 1]
            if res < d:
                res = d
        
        return res