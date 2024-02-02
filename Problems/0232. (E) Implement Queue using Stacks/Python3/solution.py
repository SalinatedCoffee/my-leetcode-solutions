class MyQueue:
  # two stacks

  def __init__(self):
    # only list _a contains items when methods are called
    self._a, self._b = [], []
    # reverse is True when top of stack _a is last item in queue
    self._reverse = True

  def _flip(self):
    # move contents of _a into _b and swap the stacks
    while self._a:
      self._b.append(self._a.pop())
    self._a, self._b = self._b, self._a
    self._reverse ^= True

  def push(self, x: int) -> None:
    if not self._reverse:
      self._flip()
    self._a.append(x)

  def pop(self) -> int:
    if self._reverse:
      self._flip()
    return self._a.pop()

  def peek(self) -> int:
    if self._reverse:
      self._flip()
    return self._a[-1]

  def empty(self) -> bool:
    return len(self._a) == 0

