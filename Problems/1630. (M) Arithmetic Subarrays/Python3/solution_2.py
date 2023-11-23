class Solution:
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    # brute force with sets

    ret = []
    for l_i, r_i in zip(l, r):
      s_a = set(nums[l_i:r_i+1])
      l, h = min(s_a), max(s_a)
      if (h - l) % (r_i - l_i) != 0:
        ret.append(False)
        continue
      d = (h - l) // (r_i - l_i)
      c = l + d
      while c < h:
        if c not in s_a:
          break
        c += d
      ret.append(True if c == h else False)
    
    return ret

