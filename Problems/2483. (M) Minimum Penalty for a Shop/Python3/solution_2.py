class Solution:
  def bestClosingTime(self, customers: str) -> int:
    # single pass

    ret, cur = 0, 0
    min_pen = 0
    for i, c in enumerate(customers):
      cur += 1 if c == 'N' else -1
      if cur < min_pen:
        min_pen = cur
        ret = i+1

    return ret

