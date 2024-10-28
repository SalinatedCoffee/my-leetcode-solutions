class Solution:
  def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
    # recursion

    # heights[i] is max height of tree after node i is removed
    heights = defaultdict(int)
    # current maximum height
    self.cur_max = 0
    # perform DFS traversal on tree while computing maximum height after removal
    def recurse(node, cur, l2r = True):
      if node is None:
        return
      heights[node.val] = self.cur_max if l2r is True else max(heights[node.val], self.cur_max)
      self.cur_max = max(self.cur_max, cur)

      if l2r is True:
        recurse(node.left, cur + 1)
      recurse(node.right, cur + 1, l2r)
      if l2r is False:
        recurse(node.left, cur + 1, l2r)
    
    # traverse tree twice in different directions
    recurse(root, 0)
    self.cur_max = 0
    recurse(root, 0, False)

    return [heights[query] for query in queries]

