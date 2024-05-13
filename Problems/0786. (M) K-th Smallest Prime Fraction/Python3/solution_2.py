class Solution:
  def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    # optimized min heap

    n = len(arr)
    heap = []
    for i in range(n):
      heappush(heap, (arr[i] / arr[-1], i, n-1))
    
    for _ in range(k - 1):
      _, n_idx, d_idx = heappop(heap)
      d_idx -= 1
      if d_idx > n_idx:
        heappush(heap, (arr[n_idx] / arr[d_idx], n_idx, d_idx))

    return [arr[heap[0][1]], arr[heap[0][2]]]

