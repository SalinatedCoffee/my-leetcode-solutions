class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    # greedy algorithm on sorted list

    return sum([i for i in sorted(piles, reverse=True)[1:-len(piles)//3:2]])

