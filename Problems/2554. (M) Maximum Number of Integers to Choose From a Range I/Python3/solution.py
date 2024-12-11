class Solution:
  def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    # brute force using set

    banned = set(banned)
    res = 0
    for i in range(1, n+1):
      if i not in banned:
        # adding current number would exceed maxSum
        if maxSum - i < 0:
          return res
        maxSum -= i
        res += 1

    return res

