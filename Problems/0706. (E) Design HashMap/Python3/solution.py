class MyHashMap:
  # naive single-collision implementation

  def __init__(self):
    self._buckets = [None] * 1001

  def put(self, key: int, value: int) -> None:
    b, i = key // 1000, key % 1000
    if self._buckets[b] is None:
      self._buckets[b] = [None] * 1000
    self._buckets[b][i] = value

  def get(self, key: int) -> int:
    b, i = key // 1000, key % 1000
    if self._buckets[b] is None:
      return -1
    if self._buckets[b][i] is None:
      return -1
    return self._buckets[b][i]

  def remove(self, key: int) -> None:
    b, i = key // 1000, key % 1000
    if self._buckets[b] is None:
      return
    self._buckets[b][i] = None

