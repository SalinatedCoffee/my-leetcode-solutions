class Solution:
  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    # iterative postorder(LRN) traversal

    # sanity check
    if root is None:
      return []
    
    ret = []
    pre = None
    d = 0
    nodes = []
    while root or nodes:
      # add empty list for current level if it does not exist
      if len(ret) < d+1:
        ret.append([])
      # push node onto stack and move to its left child
      if root:
        nodes.append((root, d))
        root = root.left
        d += 1
      # current node is none, look at node on top of stack
      else:
        root, d = nodes[-1]
        # if right child of node does not exist, or has already been traversed
        # then value of current node needs to be printed
        if root.right is None or root.right is pre:
          ret[d].append(root.val)
          nodes.pop()
          pre = root
          root = None
        # otherwise, explore right subtree without popping parent node from stack
        else:
          root = root.right
          d += 1

    ret.pop()

    return reversed(ret)

