class Solution:
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    # brute force

    ret = []
    for l_i, r_i in zip(l, r):
      s_a = nums[l_i:r_i+1]
      s_a.sort()
      d = s_a[1] - s_a[0]
      f = True
      for i in range(2, len(s_a)):
        if s_a[i] - s_a[i-1] != d:
          f = False
          break
      ret.append(f)
    
    return ret

