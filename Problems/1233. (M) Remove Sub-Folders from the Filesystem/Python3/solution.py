class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    # trie (prefix tree)

    # trie node
    class _Node:
      def __init__(self):
        self.word = False
        self.children = {}
    
    # populate trie
    root = _Node()
    for path in folder:
      cur = root
      folders = path.split('/')
      for f in folders:
        if f not in cur.children:
          cur.children[f] = _Node()
        cur = cur.children[f]
      cur.word = True
    
    # traverse trie
    res = []
    cur = []
    def recurse(node):
      if node.word:
        res.append("/".join(cur))
        return
      for f, n in node.children.items():
        cur.append(f)
        recurse(n)
        cur.pop()

    recurse(root)

    return res

