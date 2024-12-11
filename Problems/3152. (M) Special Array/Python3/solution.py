class Solution:
  def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    # prefix preprocessing
    
    n = len(nums)

    # value of start[i] is index of first element of the continuous region
    # ending at i-th element
    start = [0] * n
    for i in range(1, n):
      if nums[i-1] % 2 == nums[i] % 2:
        start[i] = i
      else:
        start[i] = start[i-1]
    
    # queried interval is continuous when first and last element
    # have identical values in start
    res = []
    for l, h in queries:
      res.append(start[l] == start[h])

    return res

