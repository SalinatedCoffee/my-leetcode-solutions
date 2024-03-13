class Solution:
  def pivotInteger(self, n: int) -> int:
    # prefix sum

    pre = [1] * n
    for i in range(2, n+1):
      pre[i-1] = pre[i-2] + i

    for i in range(0, n):
      lhs, rhs = pre[i], pre[-1] - pre[i] + (i+1)
      if lhs == rhs:
        return i+1
    
    return -1

