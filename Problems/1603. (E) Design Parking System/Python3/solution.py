class ParkingSystem:
  def __init__(self, big: int, medium: int, small: int):
    self._l = big
    self._m = medium
    self._s = small

  def addCar(self, carType: int) -> bool:
    match carType:
      case 1:
        if self._l:
          self._l -= 1
          return True
      case 2:
        if self._m:
          self._m -= 1
          return True
      case 3:
        if self._s:
          self._s -= 1
          return True
      case _:
        return False
    return False

