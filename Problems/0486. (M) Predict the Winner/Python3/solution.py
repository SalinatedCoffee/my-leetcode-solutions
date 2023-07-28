class Solution:
  # top-down dynamic programming (memoization)

  def PredictTheWinner(self, nums: List[int]) -> bool:
    self._nums = nums
    
    return self.recurse(0, len(nums)-1) >= 0

  @cache
  def recurse(self, l, r):
    # returns maximum score difference
    # from the perspective of the player that goes first
    if l == r:
      return self._nums[l]
    l_d = self._nums[l] - self.recurse(l+1, r)
    r_d = self._nums[r] - self.recurse(l, r-1)

    return max(l_d, r_d)

