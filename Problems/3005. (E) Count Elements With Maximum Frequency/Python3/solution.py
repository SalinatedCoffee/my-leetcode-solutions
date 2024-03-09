class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    # counting sort

    buckets = Counter(nums)
    tgt = max(buckets.values())
    ret = 0
    for freq in buckets.values():
      ret += freq if freq == tgt else 0

    return ret

