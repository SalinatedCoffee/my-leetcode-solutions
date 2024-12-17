class Solution:
  def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    # greedy algorithm using max heap
    
    freq = Counter(s)
    heap = [(-ord(k), v) for k, v in freq.items()]
    heapify(heap)
    # previous character added, number of consecutive additions
    prev, rep = 0, 0
    res = []
    while heap:
      # if previously added character is at limit
      if heap[0][0] == prev and rep >= repeatLimit:
        if len(heap) == 1:
          break
        # use next greatest character
        temp = heappop(heap)
        cur, f = heappop(heap)
        heappush(heap, temp)
      else:
        cur, f = heappop(heap)
      res.append(chr(-cur))
      if prev != cur:
        prev = cur
        rep = 0
      rep += 1
      if f > 1:
        heappush(heap, (cur, f-1))

    return ''.join(res)

