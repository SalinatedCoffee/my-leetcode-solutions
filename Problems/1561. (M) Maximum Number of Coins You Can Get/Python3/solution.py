class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    # greedy algorithm on sorted list

    r = len(piles) // 3 * 2 + 1
    piles.sort(reverse=True)
    ret = 0
    for i in range(1, r, 2):
      ret += piles[i]

    return ret

