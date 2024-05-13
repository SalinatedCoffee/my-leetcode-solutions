class Solution:
  def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    # min heap

    n = len(arr)
    heap = []
    for i in range(n):
      for j in range(i+1, n):
        heappush(heap, (arr[i] / arr[j], [arr[i], arr[j]]))
    
    for _ in range(k-1):
      heappop(heap)

    return heap[0][1]

