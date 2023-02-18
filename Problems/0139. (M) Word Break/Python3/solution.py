class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # dp with tries

    # string is one character, just search directly
    if len(s) == 1:
      return s in wordDict

    # Trie node
    class Node:
      def __init__(self):
        self.children = [None] * len(string.ascii_lowercase)
        self.last = False
    
    ctoi = lambda x: ord(x)-97

    def insert(node, word):
      for c in word:
        if not node.children[ctoi(c)]:
          node.children[ctoi(c)] = Node()
        node = node.children[ctoi(c)]
      node.last = True

    def find(node, word):
      for c in word:
        if not node.children[ctoi(c)]:
          return False
        node = node.children[ctoi(c)]
      return node.last

    root = Node()
    for word in wordDict:
      insert(root, word)
    
    # value of dp[i] is whether s[0:i] is splittable
    dp = [False] * (len(s)+1)
    # empty string is always splittable
    dp[0] = True
    for i in range(len(s)):
      for j in range(i+1):
        dp[i+1] |= find(root, s[j:i+1]) and dp[j]
    return dp[-1]

