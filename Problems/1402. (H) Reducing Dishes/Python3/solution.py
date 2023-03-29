class Solution:
  def maxSatisfaction(self, satisfaction: List[int]) -> int:
    # greedy dynamic programming
    
    satisfaction.sort()

    max_satisf = 0
    suffix_sum = 0
    i = len(satisfaction)-1
    # exit early when suffix sum becomes negative
    while i >= 0 and suffix_sum + satisfaction[i] > 0:
      suffix_sum += satisfaction[i]
      max_satisf += suffix_sum
      i -= 1
    
    return max_satisf

