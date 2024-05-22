class Solution:
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    # greedy algorithm on sorted list with max heap

    n = len(quality)
    # list of tuples that contain wage-to-quality ratio and quality
    # sorted by wage-to-quality ratio in ascending order
    ratios = [(wage[i]/quality[i], quality[i]) for i in range(n)]
    ratios.sort()
    # max heap containing quality values of currently hired workers
    heap = []
    ret, cur = float('inf'), 0
    for r, q in ratios:
      heappush(heap, -q)
      cur += q
      if len(heap) > k:
        # remove worker with highest quality
        cur += heappop(heap)
      if len(heap) == k:
        # calculate total cost and update minimum if applicable
        ret = min(ret, cur * r)
    
    return ret

