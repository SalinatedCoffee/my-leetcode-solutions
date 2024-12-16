class Solution:
  def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    # min heap

    n = len(nums)
    nums = [(nums[i], i) for i in range(n)]
    heapify(nums)
    # apply k operations
    for _ in range(k):
      v, i = heappop(nums)
      heappush(nums, (v*multiplier, i))
    
    # reconstruct nums
    res = [0] * n
    for v, i in nums:
      res[i] = v

    return res

