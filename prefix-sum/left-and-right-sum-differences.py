class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0 
        suffix = sum(nums)
        ans = []

        for n in nums: 
            prefix += n
            ans.append(abs(prefix - suffix))
            suffix -= n
            
        return ans