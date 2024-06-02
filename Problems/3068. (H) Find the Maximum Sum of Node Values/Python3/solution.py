class Solution:
  def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)

    n = len(nums)

    @cache
    def recurse(idx, even):
      # return maximum sum of nums[idx:] where
      #   if even == True, the number of selected nodes is even
      #   otherwise, the number of selected nodes is odd
      if idx == n:
        return 0 if even else float('-inf')
      ret = nums[idx] + recurse(idx+1, even)
      return max(ret, (nums[idx] ^ k) + recurse(idx+1, even ^ True))
    
    return recurse(0, True)

