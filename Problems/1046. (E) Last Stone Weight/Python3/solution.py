class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    # heap queue

    # Python max heap hack
    # yes, there probably is a better way of doing this
    hq = [-1*i for i in stones]
    heapify(hq)

    while len(hq) > 1:
      y = heappop(hq) * -1
      x = heappop(hq) * -1
      if x == y:
        continue
      heappush(hq, -1*(y-x))

    return 0 if not hq else -1*hq[0]

