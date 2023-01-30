class Solution:
    def tribonacci(self, n: int) -> int:
      # memoize previously computed values

      # sanity check
      if n == 0:
        return 0
      if n <= 2:
        return 1
      
      # init dp vars
      dp_0, dp_1, dp_2 = 0, 1, 1

      # compute up to n-th number
      for i in range(3, n+1):
        dp = dp_0 + dp_1 + dp_2
        dp_0, dp_1, dp_2 = dp_1, dp_2, dp
      
      return dp_2

