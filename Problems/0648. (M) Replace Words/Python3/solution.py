class Solution:
  # trie (prefix tree) with dictionaries under the hood
  class Trie:
    class TrieNode:
      def __init__(self):
        self.children = {}
        self.end = False

    def __init__(self):
      self.root = self.TrieNode()
    
    def add(self, word):
      # add word to trie
      cur = self.root
      for c in word:
        if c not in cur.children:
          cur.children[c] = self.TrieNode()
        cur = cur.children[c]
      cur.end = True

    def match(self, word):
      # find and return earliest prefix match of word in trie
      # return value is index of last character of prefix + 1
      cur = self.root
      d = 0
      for c in word:
        if c not in cur.children or cur.end:
          break
        cur = cur.children[c]
        d += 1
      return d if cur.end else -1

  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    TRIE = self.Trie()
    # add words in dictionary to trie
    for word in dictionary:
      TRIE.add(word)
    
    # split sentence into words, then find and replace words that have a prefix
    words = sentence.split()
    for i in range(len(words)):
      idx = TRIE.match(words[i])
      if idx > 0:
        words[i] = words[i][:idx]

    # concatenate words back into string
    return ' '.join(words)

