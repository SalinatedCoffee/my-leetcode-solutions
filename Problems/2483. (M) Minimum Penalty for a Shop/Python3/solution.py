class Solution:
  def bestClosingTime(self, customers: str) -> int:
    # prefix / suffix sums (two-pass)

    n = len(customers)
    pen = [0]*(n+1)
    cur = 0
    # compute open penalties
    for i in range(n):
      pen[i] = cur
      cur += 1 if customers[i] == 'N' else 0
    pen[-1] = cur
    cur = 0
    # compute close penalties
    for i in range(n-1, -1, -1):
      cur += 1 if customers[i] == 'Y' else 0
      pen[i] += cur
    ret, min_pen = 0, 10**5+1
    # find minimum penalty
    for i in range(n+1):
      if pen[i] < min_pen:
        min_pen = pen[i]
        ret = i

    return ret
    
