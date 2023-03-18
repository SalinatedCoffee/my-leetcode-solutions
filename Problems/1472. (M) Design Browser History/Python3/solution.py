class BrowserHistory:
  # doubly linked list

  class _HistoryNode:
    def __init__(self, url, p = None, n = None):
      self.url = url
      self.prev = p
      self.next = n

  def __init__(self, homepage: str):
    self.cur = self._HistoryNode(homepage)

  def visit(self, url: str) -> None:
    # unlink next node and attach new with url url
    if self.cur.next:
      self.cur.next.prev = None
    self.cur.next = self._HistoryNode(url, self.cur)
    self.cur.next.prev = self.cur
    self.cur = self.cur.next

  def back(self, steps: int) -> str:
    # move back steps nodes or until first node is reached
    while steps and self.cur.prev:
      self.cur = self.cur.prev
      steps -= 1
    return self.cur.url

  def forward(self, steps: int) -> str:
    # move forward steps nodes or until last node is reached
    while steps and self.cur.next:
      self.cur = self.cur.next
      steps -= 1
    return self.cur.url

