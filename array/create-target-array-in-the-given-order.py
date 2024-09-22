class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for n, i in zip(nums, index):
            result.insert(i, n)
        return result