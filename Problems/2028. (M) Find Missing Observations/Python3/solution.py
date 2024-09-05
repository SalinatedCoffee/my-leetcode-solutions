class Solution:
  def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    # math

    m = len(rolls)
    # determine whether answer exists
    tot_n = mean * (m + n) - sum(rolls)
    if tot_n < n or tot_n > (n*6):
      return []
    
    # generate list of unobserved rolls
    res = [tot_n // n] * n
    tot_n -= tot_n - tot_n % n
    idx = 0
    # distribute remainder
    while tot_n:
      d = min(tot_n, 6 - res[idx])
      res[idx] += d
      tot_n -= d
      idx += 1

    return res

