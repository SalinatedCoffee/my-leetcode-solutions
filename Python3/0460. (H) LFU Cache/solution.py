class LFUCache:
  # triple dictionaries
  def __init__(self, capacity: int):
    # key: key, value: [frequency, value]
    self._items = {}
    # key: frequency, value: dict(keys)
    self._freq = {}
    self._cap = capacity
    self._minfreq = 0

  def _insert(self, key, frequency, value):
    # insert item with given arguments
    self._items[key] = [frequency, value]
    if frequency not in self._freq:
      self._freq[frequency] = {}
    self._freq[frequency][key] = None

  def get(self, key: int) -> int:
    # item not in cache
    if key not in self._items:
      return -1
    freq, val = self._items[key]
    # delete key from frequency set
    del self._freq[freq][key]
    # if no more keys in min. frequency set
    if self._minfreq == freq and not self._freq[freq]:
      self._minfreq += 1
    self._insert(key, freq+1, val)
    return val

  def put(self, key: int, value: int) -> None:
    # was initialized with 0 capacity
    if self._cap <= 0:
      return
    # item already exists
    if key in self._items:
      self._items[key][1] = value
      # increment item frequency and update self._freq accordingly
      self.get(key)
      return
    # cache at capacity
    if self._cap == len(self._items):
      # get lru item from lfu set
      # Python dict adds items onto right side
      # next(iter(dict)) is faster than list(dict)[0]
      lru = next(iter(self._freq[self._minfreq]))
      # evict item
      del self._freq[self._minfreq][lru]
      del self._items[lru]
    # item is new to cache, update min. frequency and add item
    self._minfreq = 1
    self._insert(key, 1, value)

