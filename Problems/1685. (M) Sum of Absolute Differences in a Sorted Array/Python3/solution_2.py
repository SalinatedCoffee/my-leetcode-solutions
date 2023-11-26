class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    # optimized prefix sum

    n = len(nums)
    pre, tot = 0, sum(nums)
    
    ret = [0] * n
    for i in range(n):
      suf = tot - pre - nums[i]
      d_pre = i * nums[i] - pre
      d_suf = suf - (n - 1 - i) * nums[i]
      ret[i] = d_pre + d_suf
      pre += nums[i]
    
    return ret

