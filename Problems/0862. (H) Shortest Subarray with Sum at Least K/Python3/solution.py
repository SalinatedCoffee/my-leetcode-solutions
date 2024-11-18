class Solution:
  def shortestSubarray(self, nums: List[int], k: int) -> int:
    # min heap with rolling prefix sum

    n = len(nums)
    res = float('inf')
    cur = 0
    heap = []
    for i in range(n):
      cur += nums[i]
      # prefix ending at current element is a valid prefix
      if cur >= k:
        res = min(res, i + 1)
      # look through previous prefixes in ascending order of their sums,
      # removing valid ones from the heap while checking the length of the subarray
      while heap and cur - heap[0][0] >= k:
        res = min(res, i - heappop(heap)[1])
      heappush(heap, (cur, i))

    return -1 if res == float('inf') else res

