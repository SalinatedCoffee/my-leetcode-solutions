class Solution:
  def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
    # union find approach
    # number of paths can be computed without traversal
    # incrementally build up subgraph while accumulating path count

    n = len(vals)
    # generate adjacency list: O(n)
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    # create sorted dict that maps values to set of nodes: O(nlogn)
    vals_sorted = sorted(set(vals))
    values_to_nodes = {}
    for k in vals_sorted:
      values_to_nodes[k] = []
    for i in range(n):
      values_to_nodes[vals[i]].append(i)
    
    # union find object that supports find and merge operations
    class UFind:
      def __init__(self, size):
        self.parent = [x for x in range(size)]
        # arbitrary rank as tiebreaker
        self.rank = [0] * size
      
      # O(1)
      def find(self, x):
        if self.parent[x] != x:
          self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
      
      # O(1)
      def union_set(self, x, y):
        set_x, set_y = self.find(x), self.find(y)
        # x and y already in same set (subgraph)
        if set_x == set_y:
          return
        # merge according to rank
        elif self.rank[set_x] < self.rank[set_y]:
          self.parent[set_x] = set_y
        elif self.rank[set_x] > self.rank[set_y]:
          self.parent[set_y] = set_x
        else:
          # arbitrarily decide rank
          self.parent[set_y] = set_x
          self.rank[set_x] += 1
    
    obj = UFind(n)
    good_paths = 0
    # iterate over sets of nodes with same vals in ascending order: O(n)
    for val, nodes in enumerate(values_to_nodes.values()):
      for node in nodes:
        for n in adj[node]:
          # if neighbor has smaller value, add to node's subgraph
          if vals[node] >= vals[n]:
            obj.union_set(node, n)
      # count size of all current subgraphs: O(n)
      group = {}
      for node in nodes:
        # get unique id of subgraph where node is a member
        node_g = obj.find(node)
        # increment subgraph size
        if node_g in group:
          group[node_g] += 1
        else:
          group[node_g] = 1
      # compute number of good paths for all subgraphs: O(n)
      for c in group.values():
        good_paths += (c*(c+1)//2)
    
    return good_paths

