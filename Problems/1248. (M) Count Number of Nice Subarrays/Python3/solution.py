class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    # sliding window with dictionary

    # pre_freq[i] is number of prefixes before current that contains i odd values
    pre_freq = defaultdict(int)
    pre_freq[0] = 1
    ret, cur = 0, 0
    for num in nums:
      if num % 2:
        cur += 1
      # if there are prefixes that can make the current contain k odd values,
      # count them
      ret += pre_freq[cur-k]
      pre_freq[cur] += 1

    return ret

