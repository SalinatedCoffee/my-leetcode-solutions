class Solution:
  def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    # top-down dynamic programming (tabulation)

    n = len(nums1)
    m = len(nums2)
    # dp[i][j] is value of recurse(i, j)
    dp = [[-1] * m for _ in range(n)]

    def recurse(i, j):
      # returns max. number of lines between nums1[:i+1] and nums2[:j+1]
      if i < 0 or j < 0:
        return 0
      
      if dp[i][j] != -1:
        return dp[i][j]
      
      if nums1[i] == nums2[j]:
        dp[i][j] = 1 + recurse(i-1, j-1)
      else:
        dp[i][j] = max(recurse(i-1, j), recurse(i, j-1))

      return dp[i][j]
    
    return recurse(n-1, m-1)

