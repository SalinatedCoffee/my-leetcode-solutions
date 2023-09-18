class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    # brute force

    m, n = len(mat), len(mat[0])
    heap = []
    for i in range(m):
      c = sum(mat[i])
      heappush(heap, (c, i))
    
    ret = []
    while k:
      ret.append(heappop(heap)[1])
      k -= 1
    
    return ret

