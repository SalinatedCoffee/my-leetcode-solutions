class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    # brute force

    ret, maj = 0, -1
    freq = Counter(nums)
    for k, v in freq.items():
      if v > maj:
        ret, maj = k, v

    return ret

