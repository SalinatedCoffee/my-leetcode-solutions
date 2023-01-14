class Solution:
  def longestPath(self, parent: List[int], s: str) -> int:
    # adjacent nodes must be different, not entire path
    # optimal strategy is to connect two longest valid paths
    # return longest path from subtree + 1
    # longest path may not go through root, so keep track of longest path

    # generate adjacency list
    adj = [[] for _ in range(len(parent))]
    for i in range(1, len(parent)):
      adj[parent[i]].append(i)
    
    # global maximum path length
    self.max_len = 0
    def dfs(root, prev):
      # top 2 longest paths of subtrees
      res = [0, 0]
      for i in adj[root]:
        if i == prev:
          continue
        sub = dfs(i, root)
        # adjacent node has different label, valid path
        if s[i] != s[root]:
          # update top 2 list accordingly
          if res[1] < sub:
            res[0] = res[1]
            res[1] = sub
          elif res[0] < sub:
            res[0] = sub
      # max path length at this recursion level
      total = sum(res) + 1
      self.max_len = max(total, self.max_len)
      # return longest path length of single subtree
      return res[1] + 1
    
    dfs(0, None)

    return self.max_len

