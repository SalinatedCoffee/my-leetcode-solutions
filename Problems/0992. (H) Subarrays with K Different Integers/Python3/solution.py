class Solution:
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    # two-pass sliding window

    n = len(nums)

    def at_most_K(k):
      # return number of subarrays that contain at most k unique elements
      l, ret = 0, 0
      freq = defaultdict(int)
      for i in range(n):
        freq[nums[i]] += 1
        while len(freq) > k:
          freq[nums[l]] -= 1
          if freq[nums[l]] == 0:
            del freq[nums[l]]
          l += 1
        ret += i - l + 1

      return ret

    return at_most_K(k) - at_most_K(k-1)

