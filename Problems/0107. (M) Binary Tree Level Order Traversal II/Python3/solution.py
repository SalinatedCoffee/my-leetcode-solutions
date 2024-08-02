class Solution:
  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    # recursive preorder(NLR) traversal

    # sanity check
    if root is None:
      return []

    ret = []
    def recurse(node, d, nodes):
      # add empty list for current level if it does not exist
      if len(nodes) < d:
        nodes.append([])
      nodes[d-1].append(node.val)
      if node.left:
        recurse(node.left, d+1, nodes)
      if node.right:
        recurse(node.right, d+1, nodes)
    
    recurse(root, 1, ret)

    return reversed(ret)

