class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    # optimized brute force

    n = len(nums)
    nums.sort()
    res = 0
    # fix a
    for i in range(n):
      # fix b
      for j in range(n-1, i, -1):
        prod = nums[i] * nums[j]
        cand = set()
        # fix c
        for k in range(i+1, j):
          # if a, b, and c are valid, try searching for d
          if prod % nums[k] == 0:
            tgt = prod // nums[k]
            if tgt in cand:
              res += 8
            cand.add(nums[k])

    return res

