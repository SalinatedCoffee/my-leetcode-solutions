class SummaryRanges:
  # value range is relatively small
  # use list as internal data structure
  def __init__(self):
    self._intervals = [0] * 10**4
    self._min = 10**4 + 1
    self._max = -1

  def addNum(self, value: int) -> None:
    self._intervals[value] = 1
    # update min/max as necessary
    if value < self._min:
      self._min = value
    if value > self._max:
      self._max = value

  def getIntervals(self) -> List[List[int]]:
    # sanity check
    if self._max == -1:
      return []

    ret = []
    l = self._min
    # iterate range [min, max] while generating intervals
    for i in range(self._min, self._max+1):
      if self._intervals[i] == 1:
        if l == -1:
          l = i
      elif self._intervals[i] == 0:
        if l != -1:
          ret.append((l, i-1))
          l = -1
    ret.append((l, self._max))
    
    return ret

