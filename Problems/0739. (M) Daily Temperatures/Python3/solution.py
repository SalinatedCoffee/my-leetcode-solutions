class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # monotonic stack

    n = len(temperatures)
    ret = [0] * n
    # contents of stack monotonically decreases
    stack = []
    for i in range(n-1, -1, -1):
      while stack and temperatures[stack[-1]] <= temperatures[i]:
        stack.pop()
      if stack:
        ret[i] = stack[-1] - i
      stack.append(i)

    return ret

