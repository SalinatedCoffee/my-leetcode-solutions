class KthLargest:
  # heap

  def __init__(self, k: int, nums: List[int]):
    self._items = nums
    self._k = k
    heapify(self._items)
        
  def add(self, val: int) -> int:
    heappush(self._items, val)
    while len(self._items) > self._k:
      heappop(self._items)

    return self._items[0]

