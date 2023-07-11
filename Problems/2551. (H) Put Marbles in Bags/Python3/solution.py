class Solution:
  def putMarbles(self, weights: List[int], k: int) -> int:
    # greedy with sorting

    # sanity check
    if k == 1:
      return 0

    n = len(weights)
    pair_sums = [weights[i] + weights[i+1] for i in range(n-1)]
    pair_sums.sort()

    return sum(pair_sums[-k+1:]) - sum(pair_sums[:k-1])
