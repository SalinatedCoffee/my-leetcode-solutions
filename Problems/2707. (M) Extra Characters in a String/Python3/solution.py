# top-down dynamic programming (tabulation) with tries

class TrieNode:
  def __init__(self):
    self.c = {}
    self.end = False

class Solution:
  def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    self.n = len(s)
    self.s = s
    self.root = TrieNode()
    # insert all words in trie
    for w in dictionary:
      cur = self.root
      for c in w:
        if c not in cur.c:
          cur.c[c] = TrieNode()
        cur = cur.c[c]
      cur.end = True

    return self.recurse(0)
  
  @cache
  def recurse(self, i):
    # return num of minimum extra characters for s[i:]

    if i == self.n:
      return 0
    
    ret = self.recurse(i+1) + 1
    cur = self.root
    for j in range(i, self.n):
      if self.s[j] not in cur.c:
        break
      cur = cur.c[self.s[j]]
      if cur.end:
        ret = min(ret, self.recurse(j+1))

    return ret
    
