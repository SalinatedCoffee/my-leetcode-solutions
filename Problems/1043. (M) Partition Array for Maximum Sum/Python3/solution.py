class Solution:
  def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    # top-down dynamic programming (memoization)

    n = len(arr)

    @cache
    def recurse(idx):
      # return maximum sum of partitioning arr[idx:]
      if idx >= n:
        return 0
      l_val, l_sum = -1, -1
      for i in range(min(k, n - idx)):
        l_val = max(l_val, arr[idx+i])
        l_sum = max(l_sum, l_val * (i+1) + recurse(idx+i+1))
      
      return l_sum

    return recurse(0)

