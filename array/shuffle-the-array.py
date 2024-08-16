class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result += [nums[i]]
            result += [nums[i + n]]
        
        return result