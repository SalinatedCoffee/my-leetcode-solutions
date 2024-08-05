class Solution:
  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    # priority queue
    
    MOD = 10**9 + 7
    sums = [(nums[i], i) for i in range(n)]
    heapify(sums)
    ret = 0
    for i in range(1, right+1):
      cur, idx = heappop(sums)
      # add subarray to sum if it falls within desired range
      if left <= i:
        ret = (ret + cur) % MOD
      # if possible, expand subarray by 1 towards the right
      if idx < n-1:
        heappush(sums, (cur + nums[idx+1], idx+1))

    return ret

