class Solution:
  def sortColors(self, nums: List[int]) -> None:
    # 3-way partitioning
    
    n = len(nums)
    # after sort, nums[:l] should contain only 0s
    # nums[l:h] only 1s, and nums[h+1:] only 2s
    l, m, h = 0, 0, n-1
    while m <= h:
      # match-case only available in Python 3.10+
      match nums[m]:
        case 0:
          nums[l], nums[m] = nums[m], nums[l]
          l += 1
          m += 1
        case 1:
          m += 1
        case 2:
          nums[m], nums[h] = nums[h], nums[m]
          h -= 1

