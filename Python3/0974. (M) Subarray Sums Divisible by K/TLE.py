class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    # precompute prefix sum, no need to compute sum for all subarrays
    prefix_sum = [0 for _ in range(len(nums))]

    # compute prefix sums
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
      prefix_sum[i] = prefix_sum[i-1] + nums[i]

    count = 0
    # try all subarrays
    for i in range(len(nums)-1):
      for j in range(i+1, len(nums)):
        subarr = prefix_sum[j] - prefix_sum[i]
        if not subarr % k:
          count += 1

    # try entire array
    if not sum(nums) % k:
      count += 1

    return count

