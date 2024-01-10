class Solution:
  def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    # DFS

    # convert tree into undirected graph
    adj = defaultdict(list)
    nodes = [root]
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
    
    # iterative DFS
    ret = 0
    visited = set([start])
    nodes = [(start, 0)]
    while nodes:
      cur, d = nodes.pop()
      ret = max(ret, d)
      for nxt in adj[cur]:
        if nxt not in visited:
          nodes.append((nxt, d+1))
          visited.add(nxt)

    return ret

