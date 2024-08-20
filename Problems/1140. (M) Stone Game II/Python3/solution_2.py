class Solution:
  def stoneGameII(self, piles: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(piles)
    # dp[i][j] is maximum number of stones collected by Alice
    #   where piles[i:] stones remain and M = j
    dp = [[0]*(n+1) for _ in range(n+1)]

    suf = [0] * (n+1)
    for i in range(n-1, -1, -1):
      suf[i] = piles[i] + suf[i+1]
    
    for i in range(n+1):
      dp[i][-1] = suf[i]
    
    for i in range(n-1, -1, -1):
      for m in range(n-1, 0, -1):
        for x in range(1, min(2*m, n-i)+1):
          # values of dp can also be implicitly used as Bob's score
          dp[i][m] = max(dp[i][m], suf[i] - dp[i+x][max(m, x)])
    
    return dp[0][1]

