class Solution:
  def minPairSum(self, nums: List[int]) -> int:
    # greedy algorithm on sorted list using two pointers

    n = len(nums)
    nums.sort()
    ret = -1
    for i in range(n//2):
      ret = max(ret, nums[i] + nums[-i-1])
    
    return ret

