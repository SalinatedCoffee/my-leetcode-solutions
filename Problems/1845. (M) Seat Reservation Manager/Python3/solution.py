class SeatManager:
  # min heap
  
  def __init__(self, n: int):
    self._seats = [i for i in range(1, n+1)]
    heapify(self._seats)
      
  def reserve(self) -> int:
    return heappop(self._seats)

  def unreserve(self, seatNumber: int) -> None:
    heappush(self._seats, seatNumber)

