class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    # iterative reverse inorder traversal

    res = []

    if root is None:
      return res

    nodes = [root]
    while nodes:
      cur = nodes.pop()
      res.append(cur.val)
      for child in cur.children:
        if child:
          nodes.append(child)

    return reversed(res)

