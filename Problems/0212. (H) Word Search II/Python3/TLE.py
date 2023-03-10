class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # DFS + trie

    class Node:
      def __init__(self):
        self.children = [None] * 26
        self.last = False

    ret = []
    root = Node()
    
    def find(s, node, prefix=False):
      # find word s in trie rooted at node
      # if prefix == True, treat s as prefix
      for c in s:
        idx = ord(c) - ord('a')
        if not node.children[idx]:
          return False
        node = node.children[idx]
      return node.last if not prefix else True
    
    def insert(s, node):
      # insert word s in trie rooted at node
      for c in s:
        idx = ord(c) - ord('a')
        if not node.children[idx]:
          node.children[idx] = Node()
        node = node.children[idx]
      node.last = True
    
    def delete(s, node):
      # delete word s in trie rooted at node
      # trims node for s[-1] if it is leaf
      prev = None
      for c in s:
        idx = ord(c) - ord('a')
        prev = node
        node = node.children[idx]
      for d in node.children:
        if d:
          node.last = False
          return
      prev.children[idx] = None

    def dfs(r, c, s, v):
      # recursive DFS
      v.add((r,c))
      if not find(s, root, True):
        v.remove((r,c))
        return
      if find(s, root):
        ret.append(s)
        delete(s, root)
      adj = [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]
      for n_r, n_c in adj:
        if 0 <= n_r < len(board) and 0 <= n_c < len(board[0]):
          if (n_r, n_c) not in v:
            dfs(n_r, n_c, s+board[n_r][n_c], v)
      v.remove((r,c))

    for word in words:
      insert(word, root)

    for i in range(len(board)):
      for j in range(len(board[0])):
        dfs(i, j, board[i][j], set())
    
    return ret

