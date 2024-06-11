class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    # iterative BFS

    # sanity check
    if root is None:
      return

    nodes = deque([(root.left, 1), (root.right, 1)])
    n_prev, d_prev = root, 0
    while nodes:
      cur, d = nodes.popleft()
      if cur is None:
        continue
      n_prev.next = cur if d == d_prev else None
      n_prev, d_prev = cur, d
      nodes.append((cur.left, d+1))
      nodes.append((cur.right, d+1))
    
    return root

