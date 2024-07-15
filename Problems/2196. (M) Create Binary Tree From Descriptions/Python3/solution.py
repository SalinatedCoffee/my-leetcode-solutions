class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    # dictionary

    # nodes[i] is TreeNode with i as its value
    nodes = {}
    has_parent = set()
    for p, c, l in descriptions:
      # create node if it doesn't exist
      if p not in nodes:
        nodes[p] = TreeNode(p)
      if c not in nodes:
        nodes[c] = TreeNode(c)
      # link nodes accordingly
      if l:
        nodes[p].left = nodes[c]
      else:
        nodes[p].right = nodes[c]
      has_parent.add(c)

    # find root node
    for k in nodes.keys():
      if k not in has_parent:
        return nodes[k]

    # this line is never reached given problem constraints
    return None

