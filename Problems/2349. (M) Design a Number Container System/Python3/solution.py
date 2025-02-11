class NumberContainers:
  # maps with min heap

  def __init__(self):
    # value of _i2v[i] is number at index i
    self._i2v = {}
    # value of _v2is[v] is min heap of indices with number v
    self._v2is = defaultdict(list)

  def change(self, index: int, number: int) -> None:
    self._i2v[index] = number
    heappush(self._v2is[number], index)

  def find(self, number: int) -> int:
    if number not in self._v2is:
      return -1
    while self._v2is[number]:
      idx = self._v2is[number][0]
      if self._i2v[idx] == number:
        return idx
      heappop(self._v2is[number])
    return -1

