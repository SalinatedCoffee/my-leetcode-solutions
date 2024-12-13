class Solution:
  def findScore(self, nums: List[int]) -> int:
    # priority queue with set

    n = len(nums)
    nums = [(nums[i], i) for i in range(n)]
    heapify(nums)
    marked = set()
    res = 0
    while nums:
      v, idx = heappop(nums)
      if idx not in marked:
        res += v
        marked.update([idx-1, idx, idx+1])

    return res

