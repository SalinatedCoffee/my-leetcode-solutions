class Solution:
  def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    # sliding window

    n = len(nums)
    # teehee
    nums.append(float('-inf'))
    # for any given i-th element of nums
    # length of longest strictly increasing subarray with i-k-th element as its last item
    lower = 0
    # length of longest strictly increasing subarray with i-th element as its last item
    upper = 1
    # initialize window
    for i in range(1, k):
      if nums[i-1] < nums[i]:
        upper += 1
      else:
        upper = 1
    # sliding window
    for i in range(k, n):
      if nums[i-1] < nums[i]:
        upper += 1
      else:
        upper = 1
      if nums[i-k-1] < nums[i-k]:
        lower += 1
      else:
        lower = 1
      if upper >= k and lower >= k:
        return True

    return False

