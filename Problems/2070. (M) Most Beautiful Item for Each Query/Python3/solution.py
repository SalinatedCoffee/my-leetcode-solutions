class Solution:
  def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    # binary search on sorted list

    # sort items in ascending order of price
    items.sort(key=lambda x: x[0])
    # determine max beauty for each unique price
    items_unique = defaultdict(int)
    b_max = 0
    for p, b in items:
      b_max = max(b_max, b)
      items_unique[p] = max(items_unique[p], b_max)
    
    # sort max beauties in ascending order of unique price
    items_unique = sorted(list(items_unique.items()))
    
    res = []
    n = len(items_unique)
    for query in queries:
      # use binary search to process query
      if query >= items_unique[0][0]:
        idx = min(n-1, bisect_left(items_unique, query, key=lambda x: x[0]))
        if items_unique[idx][0] > query:
          idx -= 1
        res.append(items_unique[idx][1])
      else:
        res.append(0)

    return res

