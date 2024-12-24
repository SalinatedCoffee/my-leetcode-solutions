class Solution:
  def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
    # priority queue (min heap)

    n, m = len(heights), len(queries)
    heap = []
    res = [-1] * m
    height_to_query = [[] for _ in range(n)]
    # preprocess queries
    for i in range(m):
      a, b = queries[i]
      # trivial queries
      if a < b and heights[a] < heights[b]:
        res[i] = b
      elif a > b and heights[a] > heights[b]:
        res[i] = a
      elif a == b:
        res[i] = a
      # queries that require further investigation
      else:
        height_to_query[max(a, b)].append((max(heights[a], heights[b]), i))
    
    for i in range(n):
      while heap and heap[0][0] < heights[i]:
        _, q_i = heappop(heap)
        res[q_i] = i
      for query in height_to_query[i]:
        heappush(heap, query)

    return res

