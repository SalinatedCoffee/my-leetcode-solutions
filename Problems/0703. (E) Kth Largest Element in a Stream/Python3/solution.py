class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    # heap
    nums.sort()
    self._items = nums[-k:]
    heapify(self._items)
    self._k = k

  def add(self, val: int) -> int:
    if len(self._items) < self._k:
      heappush(self._items, val)
    elif val > self._items[0]:
      heapreplace(self._items, val)
    return self._items[0]

