class MyCircularDeque:
  # simulated deque
  
  def __init__(self, k: int):
    self._items = [-1] * k
    self._size = 0
    self._head = 0
    self._tail = 1 % k

  def insertFront(self, value: int) -> bool:
    if self._size == len(self._items):
      return False
    self._items[self._head] = value
    self._head = (self._head + len(self._items) - 1) % len(self._items)
    self._size += 1

    return True

  def insertLast(self, value: int) -> bool:
    if self._size == len(self._items):
      return False
    self._items[self._tail] = value
    self._tail = (self._tail + len(self._items) + 1) % len(self._items)
    self._size += 1

    return True

  def deleteFront(self) -> bool:
    if self._size == 0:
      return False
    self._head = (self._head + len(self._items) + 1) % len(self._items)
    self._items[self._head] = -1
    self._size -= 1

    return True

  def deleteLast(self) -> bool:
    if self._size == 0:
      return False
    self._tail = (self._tail + len(self._items) - 1) % len(self._items)
    self._items[self._tail] = -1
    self._size -= 1

    return True

  def getFront(self) -> int:
    return self._items[(self._head + 1) % len(self._items)]

  def getRear(self) -> int:
    return self._items[self._tail - 1]

  def isEmpty(self) -> bool:
    return self._size == 0

  def isFull(self) -> bool:
    return self._size == len(self._items)

