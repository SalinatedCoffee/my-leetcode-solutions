class Solution:
  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    # brute force
    
    MOD = 10**9 + 7
    # compute sums of all possible subarrays
    sums = []
    for i in range(n):
      cur = 0
      for j in range(i, n):
        cur += nums[j]
        sums.append(cur)
    
    sums.sort()

    return sum(sums[left-1:right]) % MOD

