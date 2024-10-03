class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    # brute force with prefix sums

    n = len(nums)
    # pre[i] is sum of all elements in the prefix array nums[:i+1]
    pre = [0] * (n+1)
    pre[0] = nums[0]
    for i in range(1, n):
      pre[i] = pre[i-1] + nums[i]
    # check for edge case
    if pre[-2] % p == 0:
      return 0
    # consider all possible subarrays starting with those of length 1
    for i in range(1, n):
      for j in range(i-1, n):
        if (pre[-2] - pre[j] + pre[j-i]) % p == 0:
          return i

    return -1

