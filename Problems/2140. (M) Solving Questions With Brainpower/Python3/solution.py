class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(questions)
    # dp[i] is maximum score solving problems in questions[i:]
    dp = [0] * n
    dp[-1] = questions[-1][0]

    for i in range(n-2, -1, -1):
      dp[i], c_s = questions[i]
      if i + c_s + 1 < n:
        dp[i] += dp[i + c_s + 1]
      dp[i] = max(dp[i], dp[i+1])

    return dp[0]

