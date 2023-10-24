class Solution:
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    # iterative BFS

    # sanity check
    if root is None:
      return []

    rowmax = defaultdict(lambda: float('-inf'))
    nodes = deque([(root, 0)])
    while nodes:
      cur, l = nodes.popleft()
      rowmax[l] = max(rowmax[l], cur.val)
      if cur.left is not None:
        nodes.append((cur.left, l+1))
      if cur.right is not None:
        nodes.append((cur.right, l+1))
    
    return [v for k, v in sorted(rowmax.items())]

