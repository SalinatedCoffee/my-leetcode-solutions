class Solution:
  def longestDiverseString(self, a: int, b: int, c: int) -> str:
    # greedy with max heap

    # populate heap
    heap = []
    rem = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
    for r, ch in rem:
      if r < 0:
        heappush(heap, (r, ch))
    
    # construct string
    res = []
    while heap:
      r, ch = heappop(heap)
      # adding character would result in 3 identical consecutive characters
      if len(res) >= 2 and res[-2] == ch and res[-1] == ch:
        if not heap:
          break
        r1, ch1 = heappop(heap)
        res.append(ch1)
        if r1+1 < 0:
          heappush(heap, (r1+1, ch1))
        heappush(heap, (r, ch))
      # current character can be added
      else:
        res.append(ch)
        if r+1 < 0:
          heappush(heap, (r+1, ch))

    return "".join(res)

