class Solution:
  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    # recursive DFS

    self.path = []
    self.start = []
    self.dest = []

    def recurse(node, symbol=""):
      # find nodes with startValue or destValue by performing recursive DFS
      # on tree rooted at node, where symbol is 'L' if node is a left child 
      # or 'R' if it is a right child
      self.path.append((node.val, symbol))
      if node.val == startValue:
        self.start = self.path[:]
      elif node.val == destValue:
        self.dest = self.path[:]
      if node.left:
        recurse(node.left, 'L')
      if node.right:
        recurse(node.right, 'R')
      self.path.pop()

    # find paths from root to start and destination nodes
    recurse(root)
    # truncate identical section between both paths
    m, n = len(self.start), len(self.dest)
    i, j = 0, 0
    while i < m and j < n:
      if self.start[i][0] != self.dest[j][0]:
        break
      i += 1
      j += 1

    return 'U'*(m - i) + ''.join([s[1] for s in self.dest[j:]])

