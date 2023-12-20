class Solution:
  def buyChoco(self, prices: List[int], money: int) -> int:
    # greedy linear search

    a, b = float('inf'), float('inf')
    for p in prices:
      if p < a:
        a, b = p, a
      else:
        b = min(b, p)
    
    ret = money - a - b

    return ret if ret >= 0 else money

