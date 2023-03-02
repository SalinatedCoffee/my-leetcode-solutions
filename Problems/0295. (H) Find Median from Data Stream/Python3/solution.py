class MedianFinder:
  # double heaps

  def __init__(self):
    # smaller half, max heap
    self._l = []
    # larger half, min heap
    self._r = []
      
  def addNum(self, num: int) -> None:
    # both heaps empty
    if not len(self._l):
      heappush(self._l, -num)
      return
    # if num is smaller than top of smaller half, insert there
    if -num > self._l[0]:
      heappush(self._l, -num)
    else:
      heappush(self._r, num)
    # if size difference of heaps is larger than 1, balance
    if abs(len(self._l) - len(self._r)) > 1:
      if len(self._l) > len(self._r):
        temp = heappop(self._l)
        heappush(self._r, -temp)
      else:
        temp = heappop(self._r)
        heappush(self._l, -temp)

  def findMedian(self) -> float:
    # return top of larger heap
    if len(self._l) > len(self._r):
      return -self._l[0]
    elif len(self._r) > len(self._l):
      return self._r[0]
    # or return average of both tops
    else:
      return (-self._l[0] + self._r[0]) / 2

