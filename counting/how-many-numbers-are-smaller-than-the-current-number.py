class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i:
                    total += 1
            result.append(total)

        return result