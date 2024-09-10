class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            a = min(nums)
            nums.remove(a)

            b = min(nums)
            nums.remove(b)

            result.append(b)
            result.append(a)

        return result