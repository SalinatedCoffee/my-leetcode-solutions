class Solution:
  def canSortArray(self, nums: List[int]) -> bool:
    # sliding window

    n = len(nums)
    # largest value of previous window
    prev = 0
    # number of set bits for items in the current window
    # NOTE: int.bit_count() is supported by Python 3.10+
    #       for older versions, use bin(n).count("1")
    cur_bits = nums[0].bit_count()
    # smallest and largest value in the current window
    win_min, win_max = nums[0], nums[0]
    for i in range(n):
      if nums[i].bit_count() == cur_bits:
        win_min = min(win_min, nums[i])
        win_max = max(win_max, nums[i])
      else:
        if prev >= win_min:
          return False
        prev = win_max
        win_min, win_max = nums[i], nums[i]
        cur_bits = nums[i].bit_count()

    # examine last interval
    return prev < win_min

