class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # modified Kadane's algorithm (dynamic programming)

    min_price = 10**4
    max_prof = 0
    for p in prices:
      if p < min_price:
        min_price = p
      else:
        max_prof = max(max_prof, p - min_price)
    
    return max_prof

