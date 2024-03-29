class Solution:
  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    # sliding window with dictionary

    n = len(nums)
    l, ret = 0, 0
    counts = defaultdict(int)
    for i in range(n):
      counts[nums[i]] += 1
      while l < i and counts[nums[i]] > k:
        counts[nums[l]] -= 1
        l += 1
      ret = max(ret, i - l + 1)

    return ret

