class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            currentWealth = 0
            for b in customer:
                currentWealth += b

            maxWealth = max(maxWealth, currentWealth)
        
        return maxWealth