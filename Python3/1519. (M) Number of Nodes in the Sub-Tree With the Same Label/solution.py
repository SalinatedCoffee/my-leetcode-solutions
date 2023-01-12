class Solution:
  def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
    # DFS based traversal
    # node numbering might not be in hierarchical order

    # generate adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    # init return list
    count = [0 for _ in range(n)]
    # recursive DFS
    def dfs(root, prev):
      state = [0 for _ in range(26)]
      for i in adj[root]:
        if i == prev:
          continue
        # collate label count lists of all descendant nodes
        state = list(map(operator.add, dfs(i, root), state))
      # count label of current node
      # labels are in lowercase english alphabet, use ASCII code as index
      state[ord(labels[root])-97] += 1
      # update return list
      count[root] = state[ord(labels[root])-97]
      return state
    
    # recurse
    dfs(0, None)
    
    return count

