class Solution:
  def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # 2 pass
    
    # iterative BFS that computes level sums
    level_sum = defaultdict(int)
    nodes = deque([(root, 0)])
    while nodes:
      cur, d = nodes.popleft()
      level_sum[d] += cur.val
      if cur.left:
        nodes.append((cur.left, d+1))
      if cur.right:
        nodes.append((cur.right, d+1))

    # iterative DFS that computes cousin sums
    nodes = [(root, 0)]
    while nodes:
      cur, d = nodes.pop()
      child_sum = 0
      if cur.left:
        child_sum += cur.left.val
      if cur.right:
        child_sum += cur.right.val
      if cur.left:
        cur.left.val = level_sum[d+1] - child_sum
        nodes.append([cur.left, d+1])
      if cur.right:
        cur.right.val = level_sum[d+1] - child_sum
        nodes.append([cur.right, d+1])
    # cousin sum of root is always 0
    if root:
      root.val = 0

    return root

