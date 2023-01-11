class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    # 'b' > 'a' in Python
    # naive solution that traverses columns explicitly
    # further optimizations most likely possible
    row, col = len(strs), len(strs[0])
    if row == 1:
      return 0

    count = 0
    for j in range(col):
      for i in range(1, row):
        if strs[i-1][j] > strs[i][j]:
          count += 1
          break

    return count

