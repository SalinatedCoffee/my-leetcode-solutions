class Solution:
  def maxKelements(self, nums: List[int], k: int) -> int:
    # max heap

    # convert nums into max heap
    items = [-i for i in nums]
    heapify(items)
    res = 0
    # greedily perform k operations
    while k:
      res -= items[0]
      heappush(items, -ceil(-heappop(items) / 3))
      k -= 1

    return res

