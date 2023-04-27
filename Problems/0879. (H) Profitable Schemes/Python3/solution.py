class Solution:
  def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    # top-down dynamic programming (memoization)

    mod = 10**9 + 7
    # dp[i][j][k] is number of schemes starting at the ith crime, jth member, and k profit
    dp = [[[-1] * 101 for _ in range(101)] for _ in range(101)]

    def recurse(pos, count, curProfit):
      if pos == len(group):
        return 1 if curProfit >= minProfit else 0
      if dp[pos][count][curProfit] != -1:
        return dp[pos][count][curProfit]
      
      totalWays = recurse(pos+1, count, curProfit)
      if count + group[pos] <= n:
        totalWays += recurse(pos+1, count+group[pos], min(minProfit, curProfit+profit[pos]))
      
      dp[pos][count][curProfit] = totalWays % mod
      return dp[pos][count][curProfit]
    
    return recurse(0, 0, 0)

