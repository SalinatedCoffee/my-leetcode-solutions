class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    # BFS, copy neighbor if unvisited before pushing to queue

    if node is None:
      return None
    
    nodes = deque()
    nodes.append(node)
    # copy 'root' node
    copied = {node.val: Node(node.val)}
    while nodes:
      cur = nodes.pop()
      for adj in cur.neighbors:
        # node not copied yet
        if adj.val not in copied:
          copied[adj.val] = Node(adj.val)
          nodes.append(adj)
        copied[cur.val].neighbors.append(copied[adj.val])
    
    return copied[1]

