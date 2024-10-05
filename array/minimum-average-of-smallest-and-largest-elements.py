class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = 0
        r = len(nums) - 1
        min_avg = float("inf")

        while l < r:
            avg = nums[l] + nums[r]
            avg = avg / 2
            min_avg = min(avg, min_avg)
            l += 1
            r -= 1
        return min_avg
