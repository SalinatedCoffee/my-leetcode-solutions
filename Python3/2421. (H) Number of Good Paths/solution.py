class Solution:
  def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
    self.count = 0
    adj = [[] for _ in range(len(vals))]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    #DFS based traversal
    #give union find up to current when descending
    #can reuse same object
    #at parent node if repr node == self, count
    #set union with self(singleton) and passed
    p = [x for x in range(len(vals))]
    def ufind(a):
      pa = p[a]
      if pa != a:
        pa = ufind(pa)
      return pa
    
    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if vals[pa] > vals[pb]:
        p[b] = pa
      elif pb > pa:
        p[a] = pb

    def dfs(root, prev):
      print(p, root, prev)
      self.count += 1
      if prev:
        pprev = ufind(prev)
        print(vals[pprev], vals[root], pprev, root)
        if vals[pprev] == vals[root]:
          self.count += 1
        uunion(root, prev)
      for i in adj[root]:
        if i == prev:
          continue
        dfs(i, root)
    print(adj)
    dfs(0, None)

    return self.count

obj = Solution()
v1 = [2,2,5,5]
e1 = [[1,0],[0,2],[3,2]]
v2 = [1,3,2,1,3]
e2 = [[0,1],[0,2],[2,3],[2,4]]
print(obj.numberOfGoodPaths(v1, e1))

