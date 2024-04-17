class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    # monotonic stack with rolling column sum

    m, n = len(matrix), len(matrix[0])
    # rolling sums of each column
    row = [0] * (n+1)
    ret = 0
    for i in range(m):
      # update column sums
      for j in range(n):
        row[j] = 0 if matrix[i][j] == '0' else row[j] + 1

      # monotonic increasing stack containing indices to sums in row
      stack = []
      for j in range(n+1):
        while stack and row[stack[-1]] > row[j]:
          # while popping items from stack, also compute area
          height = row[stack.pop()]
          # if stack is empty, row[:j] is strictly decreasing; use j as width
          # otherwise, width is difference between current and top of stack
          width = j if not stack else j - stack[-1] - 1
          ret = max(ret, height * width)
        stack.append(j)

    return ret

