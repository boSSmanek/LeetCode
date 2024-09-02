class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        su = 0

        for i in range(len(nums)):
            su += nums[i]
            result.append(su)
        
        return result

        # one-liner
        #return list(accumulate(nums))