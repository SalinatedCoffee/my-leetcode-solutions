class Solution:
  def minScoreTriangulation(self, values: List[int]) -> int:
    # top-down dynamic programming (memoization)

    # value of dp(i, j) is minimum triangulation score of vertices values[i:j+1]
    @cache
    def dp(i, j):
      if i + 2 > j:
        return 0
      if i + 2 == j:
        return values[i] * values[i+1] * values[j]
      return min((values[i] * values[k] * values[j] + dp(i, k) + dp(k, j)) for k in range(i+1, j))

    return dp(0, len(values)-1)

