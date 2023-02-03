class Solution:
  def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    # dp, memoize previously computed max scores

    # sort based on ages, then scores
    l_sorted = sorted(zip(ages, scores))

    # dp[i] is max score for rosters in range [0:i] ending with i
    dp = [x[1] for x in l_sorted]

    for i in range(len(scores)):
      for j in range(i):
        # score of i is geq to score of j
        if l_sorted[i][1] >= l_sorted[j][1]:
          # update max score at i if new score is higher
          dp[i] = max(dp[i], dp[j] + l_sorted[i][1])
    
    return max(dp)

