class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    # 'b' > 'a' in Python
    # naive solution that traverses columns explicitly
    # further optimizations most likely possible
    row, col = len(strs), len(strs[0])
    if row == 1:
      return 0
    # transpose 2d list
    strs = [[m[n] for m in strs] for n in range(col)]

    count = 0
    for column in strs:
      for i in range(1, row):
        if column[i] < column[i-1]:
          count += 1
          break

    return count

