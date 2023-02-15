class LRUCache:
  # use dict as data structure
  # python dict preserves insert order
  def __init__(self, capacity: int):
    self._cap = capacity
    self._items = {}

  def get(self, key: int) -> int:
    # key not in cache
    if key not in self._items:
      return -1
    # dicts doesn't support move-to-front, delete and readd
    value = self._items.pop(key)
    self._items[key] = value
    return value

  def put(self, key: int, value: int) -> None:
    if key in self._items:
      self._items.pop(key)
      self._items[key] = value
      return
    # cache at capacity, evict lru
    if len(self._items) == self._cap:
      # dict appends new entries to the right, first element is oldest
      key_evict = next(iter(self._items))
      del self._items[key_evict]
    self._items[key] = value

