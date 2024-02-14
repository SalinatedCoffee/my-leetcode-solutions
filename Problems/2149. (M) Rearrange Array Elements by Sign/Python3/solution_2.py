class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    # two pointers

    n = len(nums)
    ret = []
    pos, neg = 0, 0
    while pos < n and neg < n:
      while nums[pos] < 0:
        pos += 1
      ret.append(nums[pos])
      pos += 1
      while nums[neg] > 0:
        neg += 1
      ret.append(nums[neg])
      neg += 1

    return ret

