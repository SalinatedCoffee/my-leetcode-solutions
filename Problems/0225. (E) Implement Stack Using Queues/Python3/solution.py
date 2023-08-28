class MyStack:
  # double queues

  def __init__(self):
    self._a = deque()
    self._b = deque()
    self._last = None
      
  def push(self, x: int) -> None:
    self._a.append(x)
    self._last = x

  def pop(self) -> int:
    while len(self._a) > 1:
      self._last = self._a.popleft()
      self._b.append(self._last)
    self._a, self._b = self._b, self._a
    return self._b.popleft()

  def top(self) -> int:
    return self._last

  def empty(self) -> bool:
    return len(self._a) == 0

