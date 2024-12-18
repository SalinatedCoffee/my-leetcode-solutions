class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    # brute force

    n = len(prices)
    res = []
    for i in range(n):
      cur = prices[i]
      for j in range(i+1, n):
        if prices[j] <= prices[i]:
          cur = prices[i] - prices[j]
          break
      res.append(cur)

    return res

