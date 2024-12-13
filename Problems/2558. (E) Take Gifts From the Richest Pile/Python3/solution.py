class Solution:
  def pickGifts(self, gifts: List[int], k: int) -> int:
    # max heap

    heap = [-gift for gift in gifts]
    heapify(heap)
    for _ in range(k):
      heappush(heap, -floor(sqrt(-heappop(heap))))
    
    res = 0
    while heap:
      # we could have just used -sum(heap) here... but pop from heap for
      # portability across different languages
      res -= heappop(heap)

    return res

