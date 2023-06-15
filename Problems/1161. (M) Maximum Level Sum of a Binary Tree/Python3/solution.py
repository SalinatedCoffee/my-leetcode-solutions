class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    # iterative BFS

    nodes = deque()
    nodes.append((root, 0))
    sums = [0]
    while nodes:
      cur, l = nodes.popleft()
      if len(sums) == l:
        sums.append(0)
      sums[l] += cur.val
      if cur.left:
        nodes.append((cur.left, l+1))
      if cur.right:
        nodes.append((cur.right, l+1))

    ret = 0
    m_sum = float('-inf')
    for l in range(len(sums)-1, -1, -1):
      if sums[l] >= m_sum:
        m_sum = sums[l]
        ret = l
    
    return ret+1

