class Solution:
  def minOperations(self, nums: List[int]) -> int:
    # unoptimzed sliding window

    n = len(nums)
    res = 0
    for i in range(n-2):
      if nums[i] == 0:
        res += 1
        for d in range(3):
          nums[i+d] ^= 1

    return res if nums[-1] == nums[-2] == 1 else -1

