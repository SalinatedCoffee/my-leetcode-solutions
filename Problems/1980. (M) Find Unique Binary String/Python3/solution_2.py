class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    # backtracking

    n = len(nums)
    nums_set = set(nums)
    def recurse(s):
      if len(s) == n:
        return s if s not in nums_set else None
      a = recurse(s + "0")
      if a is not None:
        return a
      return recurse(s + "1")

    return recurse("")

