class Solution:
  def maxProductDifference(self, nums: List[int]) -> int:
    # greedy algorithm without sorting

    a, b = float('inf'), float('inf')
    y, z = -1, -1
    for n in nums:
      if n > z:
        y, z = z, n
      else:
        y = max(n, y)
      if n < a:
        a, b = n, a
      else:
        b = min(b, n)

    return y * z - a * b

