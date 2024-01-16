class RandomizedSet:
  # dictionaries with lists
  
  def __init__(self):
    random.seed()
    self._v2i = {}
    self._i2v = []
    self._l = 0


  def insert(self, val: int) -> bool:
    if val in self._v2i:
      return False
    if self._l != 0:
      self._l -= 1
      self._i2v[self._l] = val
      self._v2i[val] = self._l
    else:
      self._i2v.append(val)
      self._v2i[val] = len(self._i2v) - 1

    return True


  def remove(self, val: int) -> bool:
    if val not in self._v2i:
      return False
    idx = self._v2i[val]
    self._i2v[idx] = self._i2v[self._l]
    self._v2i[self._i2v[idx]] = idx
    del self._v2i[val]
    self._l += 1

    return True


  def getRandom(self) -> int:
    return self._i2v[randint(self._l, len(self._i2v) - 1)]

