class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        while len(nums) > 1:
            a = min(nums)
            nums.remove(a)

            b = min(nums)
            nums.remove(b)

            result.append(b)
            result.append(a)

        if nums:
            result.append(nums[0])

        return result