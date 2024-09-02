class Solution:
  def chalkReplacer(self, chalk: List[int], k: int) -> int:
    # binary search on prefix sums

    n = len(chalk)
    # generate prefix sums of chalk
    pre = [0] * n
    pre[0] = chalk[0]
    for i in range(1, n):
      pre[i] = pre[i-1] + chalk[i]
    # reduce k if larger than sum of chalk
    if k >= pre[-1]:
      k %= pre[-1]
    
    # binary search
    return bisect_right(pre, k)

