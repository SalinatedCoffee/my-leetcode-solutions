class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    # modify given array

    ret = []
    for num in nums:
      if nums[abs(num)-1] < 0:
        ret.append(abs(num))
      else:
        nums[abs(num)-1] *= -1

    return ret

