class Solution:
  def minCost(self, n: int, cuts: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    m = len(cuts)
    cuts.sort()
    cuts.insert(0, 0)
    cuts.append(n)
    # dp[i][j] is minimum cost for all cuts between i and j
    dp = [[0] * (m+2) for _ in range(m+2)]
    
    for i in range(2, m+2):
      for l in range(m+2-i):
        r = l + i
        ans = float('inf')
        for j in range(l+1, r):
          ans = min(ans, dp[l][j]+dp[j][r]+cuts[r]-cuts[l])
        dp[l][r] = ans
    
    return dp[0][-1]

