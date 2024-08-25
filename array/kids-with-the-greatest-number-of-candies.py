class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)

        return result