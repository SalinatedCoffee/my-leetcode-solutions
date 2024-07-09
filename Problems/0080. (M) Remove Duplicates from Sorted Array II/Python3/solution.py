class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    # two pointers

    n = len(nums)
    # l points to last element in processed array
    # h points to unprocessed element currently being considered
    l, h = 0, 1
    # number of duplicates
    dupes = 1
    while h < n:
      if nums[h] == nums[l]:
        dupes += 1
      else:
        dupes = 1
      if dupes <= 2:
        l += 1
        nums[l] = nums[h]
      h += 1

    # return value should be number of processed elements
    return l + 1

