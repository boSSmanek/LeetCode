class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0

        for i in range(1 << l):
            x = 0
            for j in range(l):
                if i & (1 << j):
                    x ^= nums[j]
            count += x
        return count