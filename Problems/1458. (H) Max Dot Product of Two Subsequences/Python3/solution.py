class Solution:
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # top-down dynamic programming (memoization)

    m, n = len(nums1), len(nums2)
    # dp[i][j] is max dot product between nums1[i:] and nums2[j:]
    dp = [[None]*n for _ in range(m)]

    def recurse(i, j):
      if i == m or j == n:
        return None

      if dp[i][j] is not None:
        return dp[i][j]

      dp[i][j] = nums1[i] * nums2[j]
      a = recurse(i+1, j+1)
      b = recurse(i, j+1)
      c = recurse(i+1, j)
      if a is not None:
        dp[i][j] = max(dp[i][j], dp[i][j]+a)
      if b is not None:
        dp[i][j] = max(dp[i][j], b)
      if c is not None:
        dp[i][j] = max(dp[i][j], c)
      return dp[i][j]
    
    return recurse(0, 0)

