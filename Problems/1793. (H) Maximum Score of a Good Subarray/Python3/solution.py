class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    # greedy

    n = len(nums)
    l, h = k, k
    c_min = nums[k]
    ret = nums[k]
    while 0 < l or h < n - 1:
      if (nums[h+1] if h < n - 1 else 0) > (nums[l-1] if l else 0):
        h += 1
        c_min = min(c_min, nums[h])
      else:
        l -= 1
        c_min = min(c_min, nums[l])
      ret = max(ret, c_min * (h - l + 1))
    
    return ret

