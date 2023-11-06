class SeatManager:
  # min heap (lazy initialization)

  def __init__(self, n: int):
    self._seats = []
    self._min = 1
      
  def reserve(self) -> int:
    if self._seats:
      return heappop(self._seats)
    ret = self._min
    self._min += 1
    return ret

  def unreserve(self, seatNumber: int) -> None:
    heappush(self._seats, seatNumber)

