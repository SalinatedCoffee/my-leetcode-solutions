class Solution:
  def getAverages(self, nums: List[int], k: int) -> List[int]:
    # prefix sums

    n = len(nums)
    # p_sums[i] is prefix sum excluding nums[i]
    p_sums = [0] * (n+1)
    c_sum = 0
    for i in range(n):
      c_sum += nums[i]
      p_sums[i+1] = c_sum

    ret = [-1] * n
    for i in range(k, n-k):
      c_sum = p_sums[i+k+1] - p_sums[i-k]
      ret[i] = c_sum // (k*2+1)
    
    return ret

