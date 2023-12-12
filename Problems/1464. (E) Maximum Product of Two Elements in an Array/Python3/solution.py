class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    # brute force

    n = len(nums)
    ret = 0
    for i in range(n):
      for j in range(n):
        if i != j:
          ret = max(ret, (nums[i]-1)*(nums[j]-1))

    return ret

