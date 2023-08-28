class MyStack:
  # single queue

  def __init__(self):
    self._a = deque()
    self._last = None
      
  def push(self, x: int) -> None:
    self._a.append(x)
    self._last = x

  def pop(self) -> int:
    # rotate (pop-and-append) queue contents n-2 towards the left
    self._a.rotate(-1*(len(self._a)-2))
    # update most recently added item
    self._last = self._a.popleft()
    self._a.append(self._last)
    # remove and return desired item
    return self._a.popleft()

  def top(self) -> int:
    return self._last

  def empty(self) -> bool:
    return len(self._a) == 0

