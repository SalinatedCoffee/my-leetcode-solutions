class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    # Boyer-Moore majority vote algorithm

    val, c = 0, 0
    for num in nums:
      if val == num:
        c += 1
      elif c == 0:
        val = num
        c = 1
      else:
        c -= 1

    return val

