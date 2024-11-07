class Solution:
  def largestCombination(self, candidates: List[int]) -> int:
    # dictionary with bit manipuation

    counts = defaultdict(int)

    for candidate in candidates:
      digit = 0
      # update counts for every raised bit in the current value
      while candidate != 0:
        if candidate & 1 == 1:
          counts[digit] += 1
        candidate >>= 1
        digit += 1

    return max(counts.values())

