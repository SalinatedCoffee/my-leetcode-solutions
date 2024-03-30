class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    # sliding window

    n = len(nums)
    ret = 0
    # pre-scan for maximum value
    tgt, count = max(nums), 0
    # find first occurrence of max value
    idx = 0
    while nums[idx] != tgt:
      idx += 1
    l = idx
    # resume iterating over nums starting at max value
    while idx < n:
      if nums[idx] == tgt:
        count += 1
      # if window contains more max values than k, contract window
      if count > k:
        count -= 1
        l += 1
        while nums[l] != tgt:
          l += 1
      # if window is valid, count all subarrays towards its left
      if count == k:
        ret += (l + 1)
      idx += 1

    return ret

