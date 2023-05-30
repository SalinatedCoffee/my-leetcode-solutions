class MyHashSet:
  # store all elements in 2D list
  
  def __init__(self):
    self._items = [[] for _ in range(1000)]
    self._max = False

  def add(self, key: int) -> None:
    if key == 1000000:
      self._max = True
    else:
      mod = key % 1000
      quot = key // 1000
      if not self.contains(key):
        self._items[quot].append(mod)

  def remove(self, key: int) -> None:
    if key == 1000000:
      self._max = False
    else:
      mod = key % 1000
      quot = key // 1000
      try:
        self._items[quot].remove(mod)
      except:
        pass
      
  def contains(self, key: int) -> bool:
    if key == 1000000:
      return self._max
    mod = key % 1000
    quot = key // 1000
    return True if mod in self._items[quot] else False

