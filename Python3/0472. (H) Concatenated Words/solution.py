class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    # keep trie of all words
    # for all words, iterate and see if substring is in trie
    # if true, mark end of substring as valid concat

    # trie node
    class Node():
      def __init__(self):
        self.children = [None] * 26
        self.last = False
    
    # insert word at node node
    def insert(node, word):
      for i in word:
        idx = ord(i) - 97
        if not node.children[idx]:
          node.children[idx] = Node()
        node = node.children[idx]
      node.last = True
    
    # find word at node node
    def find(node, word):
      for i in word:
        idx = ord(i) - 97
        if not node.children[idx]:
          return False
        node = node.children[idx]
      return node.last
    
    root = Node()

    # insert all nodes in trie
    for word in words:
      insert(root, word)

    ret = []
    for word in words:
      # init dp data structure
      dp = [0] * (len(word)+1)
      # 0-th element represents prefix of empty string
      dp[0] = 1
      for i in range(len(word)):
        # current index is not end of valid concat
        if not dp[i]:
          continue
        # all substrings of range [i+1,len(word)]
        for j in range(i+1, len(word)+1):
          # if substring is not entire word and exists in trie
          if j-i < len(word) and find(root, word[i:j]):
            # mark end of substring as end of valid concat
            dp[j] = 1
        # if entire word is valid concat
        if dp[len(word)]:
          ret.append(word)
          break
    
    return ret

