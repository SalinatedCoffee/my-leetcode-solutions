class Solution:
  def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    # greedy algorithm on sorted list

    n = len(happiness)
    # sort in descending order
    happiness.sort(reverse=True)
    ret = 0
    # greedily select children in descending order of happiness
    for i in range(k):
      ret += max(0, happiness[i] - i)

    return ret

