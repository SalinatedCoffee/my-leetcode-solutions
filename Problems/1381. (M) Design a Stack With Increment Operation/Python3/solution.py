class CustomStack:
  # simulated stack

  def __init__(self, maxSize: int):
    self._items = [-1] * maxSize
    # index of top-most element + 1
    self._top = 0

  def push(self, x: int) -> None:
    if self._top < len(self._items):
      self._items[self._top] = x
      self._top += 1

  def pop(self) -> int:
    res = self._items[self._top-1]
    self._items[self._top-1] = -1
    self._top = max(self._top - 1, 0)

    return res

  def increment(self, k: int, val: int) -> None:
    for i in range(min(self._top, k)):
      self._items[i] += val

