class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    # max heap

    n = len(score)
    # string constants
    RANK_LABELS = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    ret = [None] * n
    # create max heap to sort indices in descending order of their values
    score_sorted = sorted([(-s, i) for i, s in enumerate(score)])
    # populate return list
    for i in range(n):
      ret[score_sorted[i][1]] = RANK_LABELS[i] if i < 3 else str(i+1)

    return ret

