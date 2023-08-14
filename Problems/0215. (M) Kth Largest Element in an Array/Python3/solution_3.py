class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    # counting sort

    n_min, n_max = min(nums), max(nums)
    count = [0] * (n_max - n_min + 1)
    for n in nums:
      count[n - n_min] += 1
    idx = len(count)-1
    while k > 0:
      k -= count[idx]
      idx -= 1

    return idx + n_min + 1

