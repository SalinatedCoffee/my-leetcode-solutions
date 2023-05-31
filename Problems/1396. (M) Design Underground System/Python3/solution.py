class UndergroundSystem:
  # nested dictionaries

  def __init__(self):
    self._passengers = {}
    self._stations = {}

  def checkIn(self, id: int, stationName: str, t: int) -> None:
    if id not in self._passengers:
      self._passengers[id] = (stationName, t)

  def checkOut(self, id: int, stationName: str, t: int) -> None:
    if id in self._passengers:
      origin, t1 = self._passengers[id]
      duration = t - t1
      if stationName not in self._stations:
        self._stations[stationName] = {}
      if origin not in self._stations[stationName]:
        self._stations[stationName][origin] = (duration, 1)
      else:
        d_sum, traffic = self._stations[stationName][origin]
        self._stations[stationName][origin] = (d_sum+duration, traffic+1)
      del self._passengers[id]

  def getAverageTime(self, startStation: str, endStation: str) -> float:
    if endStation in self._stations:
      if startStation in self._stations[endStation]:
        d_sum, traffic = self._stations[endStation][startStation]
        return d_sum / traffic

    # this line should never run given problem constraints
    return float('inf')

