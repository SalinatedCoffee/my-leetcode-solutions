class Solution:
  def maxScore(self, nums: List[int]) -> int:
    # top-down dynamic programming (memoization)

    memo = [-1] * (1 << len(nums))

    def recurse(mask, pairs_picked):
      if 2 * pairs_picked == len(nums):
        return 0
      if memo[mask] != -1:
        return memo[mask]

      max_score = 0

      for first_idx in range(len(nums)):
        for second_idx in range(first_idx + 1, len(nums)):
          if (mask >> first_idx) & 1 == 1 or (mask >> second_idx) & 1 == 1:
            continue
          new_mask = mask | (1 << first_idx) | (1 << second_idx)
          cur_score = (pairs_picked + 1) * math.gcd(nums[first_idx], nums[second_idx])
          rem_score = recurse(new_mask, pairs_picked+1)
          max_score = max(max_score, cur_score + rem_score)
      
      memo[mask] = max_score
      return max_score
      
    return recurse(0, 0)

