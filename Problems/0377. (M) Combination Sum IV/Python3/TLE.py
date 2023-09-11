class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    # recursion
    
    def recurse(s):
      if s == 0:
        return 1
      if s < 0:
        return 0
      ret = 0
      for n in nums:
        ret += recurse(s - n)
      return ret
    
    return recurse(target)

