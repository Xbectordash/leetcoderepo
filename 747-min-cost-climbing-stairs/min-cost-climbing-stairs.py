
class Solution:
    def solve(self, cost, n,dp):
        # Base case
        if n == 0:
           cost[0]
        if n == 1:
           cost[1]
        if n < 0:
            return 0  
        if dp[n] != -1:
            return dp[n]       
        dp[n] = cost[n] + min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
        return dp[n]   
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            n = len(cost)
            dp = [-1]*(n+1)
            ans = min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
            return ans
        