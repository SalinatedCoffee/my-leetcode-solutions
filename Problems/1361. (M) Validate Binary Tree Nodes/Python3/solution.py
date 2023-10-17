class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    # iterative BFS

    # find potential root
    p = [-1] * n
    l, r = set(leftChild), set(rightChild)
    root = -1
    for i in range(n):
      if i not in l and i not in r:
        if root != -1:
          return False
        root = i
    
    # run BFS
    nodes = deque([root])
    visited = set()
    while nodes:
      cur = nodes.popleft()
      if cur == -1:
        continue
      if cur in visited:
        return False
      visited.add(cur)
      l, r = leftChild[cur], rightChild[cur]
      nodes.append(l)
      nodes.append(r)
    
    return len(visited) == n

