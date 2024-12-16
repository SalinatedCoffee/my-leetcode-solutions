class Solution:
  def continuousSubarrays(self, nums: List[int]) -> int:
    # sliding window with dictionary

    n = len(nums)
    window = defaultdict(int)
    l, res = 0, 0
    for i in range(n):
      window[nums[i]] += 1
      while l < i and max(window.keys()) - min(window.keys()) > 2:
        window[nums[l]] -= 1
        if window[nums[l]] == 0:
          del window[nums[l]]
        l += 1
      res += i - l + 1

    return res

