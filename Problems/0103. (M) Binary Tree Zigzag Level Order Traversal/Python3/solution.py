class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS traversal with deque for each level

    # sanity check
    if not root:
      return []

    ret = []
    # queue for traversal
    nodes = deque()
    # per-level queue
    level = deque()
    nodes.append((root, 0))
    prev_depth = 0
    # node retrieval direction
    l2r = True
    while nodes:
      cur, depth = nodes.popleft()
      # depth change detected
      if depth != prev_depth:
        prev_depth = depth
        # get previous level nodes according to retrieval direction
        if l2r:
          # use list comprehension for faster appends
          ret.append([x for x in level])
        else:
          ret.append([x for x in reversed(level)])
        # flip direction
        l2r ^= True
        level.clear()
      level.append(cur.val)
      if cur.left:
        nodes.append((cur.left, depth+1))
      if cur.right:
        nodes.append((cur.right, depth+1))

    # last level doesn't trigger depth change, append manually
    if level:
      ret.append([x for x in level] if l2r else [x for x in reversed(level)])

    return ret

