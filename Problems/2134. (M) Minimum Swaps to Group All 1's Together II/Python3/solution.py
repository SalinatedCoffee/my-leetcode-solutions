class Solution:
  def minSwaps(self, nums: List[int]) -> int:
    # sliding window

    n = len(nums)
    # length of window should be equal to number of 1s in nums
    w = len(list(filter(lambda x: x == 1, nums)))

    # initialize window
    ret = float('inf')
    zeros = len(list(filter(lambda x: x == 0, nums[:w])))
    # slide window along circular array
    for i in range(w, n+w):
      ret = min(ret, zeros)
      if nums[i-w] == 0:
        zeros -= 1
      if nums[i%n] == 0:
        zeros += 1

    return ret

