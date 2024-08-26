class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    # iterative postorder traversal

    res = []

    if root is None:
      return res

    nodes = [(root, False)]
    while nodes:
      cur, visited = nodes.pop()
      if visited:
        res.append(cur.val)
      else:
        nodes.append((cur, True))
        for child in reversed(cur.children):
          if child:
            nodes.append((child, False))

    return res

