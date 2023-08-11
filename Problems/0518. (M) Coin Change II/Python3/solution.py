class Solution:
  # top-down dynamic programming (tabulation)
  def change(self, amount: int, coins: List[int]) -> int:
    self.n = len(coins)
    self.coins = coins
    self.dp = [[-1]*self.n for _ in range(amount+1)]
    return self.recurse(amount, 0)

  def recurse(self, a, u):
    # return number of combinations that add up to a
    # with coins used up to u-th coin
    if not a:
      return 1
    if u == self.n:
      return 0
    if self.dp[a][u] != -1:
      return self.dp[a][u]
    
    if self.coins[u] > a:
      self.dp[a][u] = self.recurse(a, u+1)
    else:
      self.dp[a][u] = self.recurse(a-self.coins[u], u) + self.recurse(a, u+1)

    return self.dp[a][u]

