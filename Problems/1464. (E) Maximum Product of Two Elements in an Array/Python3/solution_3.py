class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    # one pass without sorting

    a, b = -1, -1
    for num in nums:
      if num > a:
        a, b = num, a
      else:
        b = max(b, num)

    return (a-1)*(b-1)

