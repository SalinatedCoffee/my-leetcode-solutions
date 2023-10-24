class Solution:
  def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    # recursive DFS with top-down dynamic programming (memoization)

    @cache
    # return value of recurse(i) is the maximum path value starting at node i
    def recurse(i):
      if not graph[i]:
        return time[i]
      ret = 0
      for adj in graph[i]:
        ret = max(ret, recurse(adj))
      return time[i] + ret
    
    graph = defaultdict(list)
    for (x, y) in relations:
      graph[x-1].append(y-1)
    
    ret = 0
    for j in range(n):
      ret = max(ret, recurse(j))
    
    return ret

