class AllOne:
  # dictionary with doubly linked list containing sets

  # nested class for internal linked list
  class _Node:
    def __init__(self, val = 0):
      self.prev = None
      self.next = None
      self.val = val
      self.strings = set()

  def __init__(self):
    self.sentinel_head = self._Node()
    self.sentinel_tail = self._Node()
    self.sentinel_head.next = self.sentinel_tail
    self.sentinel_tail.prev = self.sentinel_head
    # maps key to its frequency node
    self.items = {}
  
  def _insert_new(self, tgt, val):
    # private method that inserts a new node with value val between tgt and tgt.next
    nxt = tgt.next
    new = self._Node(val)
    tgt.next, new.next = new, nxt
    nxt.prev, new.prev = new, tgt

    return new

  def inc(self, key: str) -> None:
    if key in self.items:
      # key already exists, move it to next frequency node
      cur = self.items[key]
      if cur.next.val != cur.val + 1:
        self._insert_new(cur, cur.val + 1)
      cur.strings.remove(key)
      # frequency node is 'vacant', clean up
      if len(cur.strings) == 0:
        p, n = cur.prev, cur.next
        p.next, n.prev = n, p
      self.items[key] = cur.next
      cur.next.strings.add(key)
    else:
      # key does not exist, assign it a frequency of 1
      if self.sentinel_head.next.val != 1:
        self._insert_new(self.sentinel_head, 1)
      self.sentinel_head.next.strings.add(key)
      self.items[key] = self.sentinel_head.next

  def dec(self, key: str) -> None:
    cur = self.items[key]
    if cur.prev.val != cur.val - 1:
      self._insert_new(cur.prev, cur.val - 1)
    cur.strings.remove(key)
    if len(cur.strings) == 0:
      p, n = cur.prev, cur.next
      p.next, n.prev = n, p
    # key now has frequency of 0, remove it from dictionary
    if cur.val == 1:
      del self.items[key]
    # otherwise, update dictionary and frequency node
    else:
      self.items[key] = cur.prev
      cur.prev.strings.add(key)

  def getMaxKey(self) -> str:
    return next(iter(self.sentinel_tail.prev.strings)) if self.items else ""

  def getMinKey(self) -> str:
    return next(iter(self.sentinel_head.next.strings)) if self.items else ""

