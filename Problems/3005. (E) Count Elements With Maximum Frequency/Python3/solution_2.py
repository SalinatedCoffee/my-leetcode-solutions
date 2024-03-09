class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    # one pass counting sort

    counts = defaultdict(int)
    max_vals = 0
    cur_max = 0
    for num in nums:
      counts[num] += 1
      if counts[num] > cur_max:
        max_vals = 1
        cur_max = counts[num]
      elif counts[num] == cur_max:
        max_vals += 1

    return max_vals * cur_max

