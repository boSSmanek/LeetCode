class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        nl = len(nums)
        for i in range(0, nl- 1):
            for j in range(i + 1, nl):
                if nums[i] == nums[j] and i < j:
                    pair += 1
        return pair