class Solution:
  def sumPrefixScores(self, words: List[str]) -> List[int]:
    # trie with frequency count

    class TrieNode:
      def __init__(self):
        self.children = {}
        self.count = 0
    
    # generate trie from list of words
    root = TrieNode()
    for word in words:
      cur = root
      for c in word:
        if c not in cur.children:
          cur.children[c] = TrieNode()
        cur = cur.children[c]
        cur.count += 1
    
    # compute score for each word
    res = []
    for word in words:
      cur = root
      score = 0
      for c in word:
        cur = cur.children[c]
        score += cur.count
      res.append(score)

    return res

