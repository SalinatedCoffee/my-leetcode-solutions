class Solution:
  def minimumOperations(self, root: Optional[TreeNode]) -> int:
    # iterative BFS, dictionary, and cycle sort

    # retrieve list of per-level node values ordered left to right
    level_values = defaultdict(list)
    nodes = deque([(root, 0)])
    while nodes:
      cur, d = nodes.popleft()
      level_values[d].append(cur.val)
      if cur.left:
        nodes.append((cur.left, d+1))
      if cur.right:
        nodes.append((cur.right, d+1))
    
    # count number of required swaps using cycle sort
    res = 0
    for vals in level_values.values():
      # sort list of values to compare against original
      target = sorted(vals)
      # quickly retrieve original index given value
      v2i = {v: i for i, v in enumerate(vals)}
      for i in range(len(vals)):
        if vals[i] != target[i]:
          res += 1
          cur = v2i[target[i]]
          v2i[vals[i]] = cur
          vals[cur] = vals[i]

    return res

