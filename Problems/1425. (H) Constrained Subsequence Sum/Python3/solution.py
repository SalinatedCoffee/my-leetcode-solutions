class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    # dynamic programming with max heap

    n = len(nums)
    heap = [(-nums[0], 0)]
    ret = nums[0]
    for i in range(1, n):
      while i - heap[0][1] > k:
        heappop(heap)
      cur = nums[i] - (heap[0][0] if heap[0][0] < 0 else 0)
      ret = max(ret, cur)
      heappush(heap, (-cur, i))
    
    return ret

