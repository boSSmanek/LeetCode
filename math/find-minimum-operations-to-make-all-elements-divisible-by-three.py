class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        for n in nums:
            r = n % 3
            if r == 1:
                op += 1
            elif r == 2:
                op += 1
                
        return op