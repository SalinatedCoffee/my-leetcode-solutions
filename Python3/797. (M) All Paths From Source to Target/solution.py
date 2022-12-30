class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    # naively traverse all items in graph
    # guaranteed to work because graph is acyclic
    # B/DFS both work, will be using DFS here
    # Push tuples ([path], cur) to stack,
    # append [path]+cur to result list when destination is reached

    # DFS stack
    stack = []
    # List of correct paths
    ret = []
    # Destination node is n-1
    dest = len(graph)-1

    # Set up source node
    for i in graph[0]:
      stack.append(([0], i))

    # Traverse
    while len(stack):
      path, cur = stack.pop()
      path.append(cur)
      # If destination node is reached
      if cur == dest:
        ret.append(path)
        continue
      # Push reachable neighbors to stack
      for i in graph[cur]:
        stack.append((path[:], i))
    
    return ret
            
