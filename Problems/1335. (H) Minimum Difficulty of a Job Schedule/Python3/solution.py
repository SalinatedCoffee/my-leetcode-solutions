class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    # top-down dynamic programming (memoization)

    n = len(jobDifficulty)
    # sanity check
    if n < d:
      return -1

    @cache
    def recurse(i, j):
      # returns min difficulty of dividing jobDifficulty[i:] into j days
      if i == n:
        return 0
      if j == 1:
        return max(jobDifficulty[i:])
      ret, k = float('inf'), -1
      for i in range(i, n - j + 1):
        k = max(k, jobDifficulty[i])
        ret = min(ret, k + recurse(i + 1, j - 1))

      return ret

    return recurse(0, d)

