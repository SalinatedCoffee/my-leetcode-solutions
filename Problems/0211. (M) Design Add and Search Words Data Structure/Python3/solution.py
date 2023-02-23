class WordDictionary:
  # prefix tree (trie) that supports wildcard search

  class Node():
    def __init__(self, last=False):
      self.children = [None] * len(string.ascii_lowercase)
      self.last = last

  def __init__(self):
    self.root = WordDictionary.Node()
    # delete unsupported, keep track of longest word in tree
    self.max_length = 0

  def addWord(self, word: str) -> None:
    # iteratively add word to trie

    cur = self.root
    for c in word:
      idx = ord(c) - ord('a')
      if cur.children[idx] is None:
        cur.children[idx] = WordDictionary.Node()
      cur = cur.children[idx]
    cur.last = True
    self.max_length = max(self.max_length, len(word))

  def search(self, word: str, node: Optional[Node] = None) -> bool:
    # sanity check
    if len(word) > self.max_length:
      return False

    if not node:
      node = self.root
    
    for i, c in enumerate(word):
      if c == '.':
        ret = False
        for descendant in node.children:
          # recurse on wildcards
          if descendant:
            ret |= self.search(word[i+1:], descendant)
        return ret

      idx = ord(c) - ord('a')
      if not node.children[idx]:
        return False
      node = node.children[idx]
    return node.last

