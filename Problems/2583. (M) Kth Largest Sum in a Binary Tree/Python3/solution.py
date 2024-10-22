class Solution:
  def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
    # iterative BFS using a dictionary

    sums = defaultdict(int)
    nodes = deque([(root, 0)])
    while nodes:
      cur, d = nodes.popleft()
      sums[d] += cur.val
      if cur.left:
        nodes.append((cur.left, d+1))
      if cur.right:
        nodes.append((cur.right, d+1))
    
    # sort level sums in descending order
    sums = sorted(sums.values(), reverse=True)
    if len(sums) < k:
      return -1

    return sums[k-1]

