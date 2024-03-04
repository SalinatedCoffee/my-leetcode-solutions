class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    # two pointers

    n = len(nums)
    ret = [0] * n
    l, r = 0, n-1
    for i in range(n-1, -1, -1):
      if nums[l]**2 >= nums[r]**2:
        ret[i] = nums[l]**2
        l += 1
      else:
        ret[i] = nums[r]**2
        r -= 1

    return ret

