class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    # recursion
    
    n = len(nums)
    tgt = reduce(lambda x, y: x | y, nums)

    def recurse(i, cur):
      if i == n:
        return 1 if cur == tgt else 0
      
      return recurse(i+1, cur) + recurse(i+1, nums[i] | cur)

    return recurse(0, 0)

