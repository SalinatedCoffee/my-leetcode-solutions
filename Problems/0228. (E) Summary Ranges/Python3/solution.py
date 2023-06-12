class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    # simple iteration

    # sanity check
    if not nums:
      return []
    if len(nums) == 1:
      return [str(nums[0])]

    ret = []
    start = nums[0]
    for i in range(1, len(nums)):
      if nums[i-1] + 1 != nums[i]:
        if nums[i-1] != start:
          ret.append(f"{start}->{nums[i-1]}")
        else:
          ret.append(str(start))
        start = nums[i]
    if start != nums[-1]:
      ret.append(f"{start}->{nums[-1]}")
    else:
      ret.append(str(start))
    
    return ret

