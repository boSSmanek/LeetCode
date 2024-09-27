class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        for n in nums:
            if n < k:
                result += 1

        return result