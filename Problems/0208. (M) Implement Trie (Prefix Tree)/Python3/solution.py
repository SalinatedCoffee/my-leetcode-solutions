class Trie:
  # vanilla implementation using explicit nodes with 26 possible children
  class Node:
    def __init__(self):
      self.children = [None]*26
      self.last = False

  def __init__(self):
    self.root = self.Node()
    self.ctoi = lambda x: ord(x) - 97

  def insert(self, word: str) -> None:
    cur = self.root
    for c in word:
      idx = self.ctoi(c)
      if not cur.children[idx]:
        cur.children[idx] = self.Node()
      cur = cur.children[idx]
    cur.last = True

  def search(self, word: str) -> bool:
    cur = self.root
    for c in word:
      idx = self.ctoi(c)
      if not cur.children[idx]:
        return False
      cur = cur.children[idx]
    return cur.last

  def startsWith(self, prefix: str) -> bool:
    cur = self.root
    for c in prefix:
      idx = self.ctoi(c)
      if not cur.children[idx]:
        return False
      cur = cur.children[idx]
    return True

