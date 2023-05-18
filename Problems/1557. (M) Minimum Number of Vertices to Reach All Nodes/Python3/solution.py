class Solution:
  def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    # adjacency list
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[v].append(u)
    
    ret = []
    for i in range(n):
      if not adj[i]:
        ret.append(i)
    
    return ret

