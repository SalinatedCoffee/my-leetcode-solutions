class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # iterative BFS

    # input size is small enough, so just allocate memory in bulk
    adj = [[] for _ in range(501)]
    nodes = [root]
    # convert tree into undirected graph
    while nodes:
      cur = nodes.pop()
      if cur.left:
        adj[cur.val].append(cur.left.val)
        adj[cur.left.val].append(cur.val)
        nodes.append(cur.left)
      if cur.right:
        adj[cur.val].append(cur.right.val)
        adj[cur.right.val].append(cur.val)
        nodes.append(cur.right)
    
    ret = []
    nodes = deque()
    nodes.append((target.val, 0))
    visited = set([target.val])
    # traverse graph
    while nodes:
      cur, d = nodes.popleft()
      if d == k:
        ret.append(cur)
        continue
      for nxt in adj[cur]:
        if nxt not in visited:
          nodes.append((nxt, d+1))
          visited.add(nxt)

    return ret

