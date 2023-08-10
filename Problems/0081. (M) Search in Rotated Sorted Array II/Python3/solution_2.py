class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    # augmented binary search
    
    n = len(nums)
    l, h = 0, n-1
    while l <= h:
      m = l + (h - l) // 2
      if nums[m] == target:
        return True
      # cannot identify where m belongs
      if nums[l] == nums[m]:
        l += 1
      else:
        m_l = nums[l] <= nums[m]
        t_l = nums[l] <= target
        # m and target are not in the same part
        if m_l ^ t_l:
          # m is in the left part
          if m_l:
            l = m + 1
          else:
            h = m - 1
        else:
          # m and target are in same part, so direct comparison is possible
          if target < nums[m]:
            h = m - 1
          else:
            l = m + 1

    return False

