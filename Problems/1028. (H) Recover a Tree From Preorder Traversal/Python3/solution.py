class Solution:
  def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
    # recursion

    # preprocess string
    depths = list(map(len, re.findall('[\-]+', traversal)))
    values = list(map(int, re.findall('[0-9]+', traversal)))
    n = len(depths)

    root = TreeNode(values[0])
    # index of next node to be added
    self.idx = 0

    def recurse(p, d):
      # add the node values[idx+1] where its parent is p and depth of parent is d

      # if next node to be added does not exist or has improper depth
      if self.idx >= n or d + 1 != depths[self.idx]:
        return
      # add node as left child of parent
      p.left = TreeNode(values[self.idx+1])
      # advance pointer
      self.idx += 1
      # recurse down left subtree
      recurse(p.left, d+1)
      # same logic for right child
      if self.idx >= n or d + 1 != depths[self.idx]:
        return
      p.right = TreeNode(values[self.idx+1])
      self.idx += 1
      recurse(p.right, d+1)

    recurse(root, 0)
  
    return root

