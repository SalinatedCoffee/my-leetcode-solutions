class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    # prefix sum

    n = len(nums)
    pre = [0] * n
    pre[0] = nums[0]
    for i in range(1, n):
      pre[i] = pre[i-1] + nums[i]
    
    ret = [0] * n
    ret[0] = pre[-1] - nums[0] * n
    for i in range(1, n):
      ret[i] = (nums[i] * (i+1) - pre[i]) + (pre[-1] - pre[i-1] - nums[i] * (n-i))
    
    return ret

