class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)
    
    n = len(questions)
    # dp[i] is maximum score up to i-th problem
    dp = [0] * n

    for i in range(n):
      dp[i] += questions[i][0]
      for j in range(0, i):
        if questions[j][1] < (i-j):
          dp[i] = max(dp[i], dp[j]+questions[i][0])

    return max(dp)

