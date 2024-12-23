class Solution:
  def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    # recursive DFS (postorder tree traversal)
    
    self.res = 0
    # construct adjacency list
    adj = defaultdict(list)
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    # return sum of subtree rooted at node modulo k
    def recurse(node, parent):
      total = values[node]
      for nxt in adj[node]:
        if nxt != parent:
          total += recurse(nxt, node)
      total %= k

      if total == 0:
        self.res += 1

      return total

    recurse(0, -1)

    return self.res

