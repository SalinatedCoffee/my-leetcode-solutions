class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # optimized binary search

    # swap if nums1 is longer
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    l, r = 0, m

    while l <= r:
      # get midpoint of each array
      m1 = (l+r) // 2
      m2 = (m+n+1) // 2 - m1

      # get values bordering midpoints
      l1_max = float('-inf') if m1 == 0 else nums1[m1-1]
      r1_min = float('inf') if m1 == m else nums1[m1]
      l2_max = float('-inf') if m2 == 0 else nums2[m2-1]
      r2_min = float('inf') if m2 == n else nums2[m2]

      # return median if bordering values are valid
      if l1_max <= r2_min and l2_max <= r1_min:
        if (m+n) % 2 == 0:
          return (max(l1_max, l2_max) + min(r1_min, r2_min)) / 2
        return (max(l1_max, l2_max))
      # or keep valid half of nums1 and try again
      elif l1_max > r2_min:
        r = m1 - 1
      else:
        l = m1 + 1

    # this line should never execute
    return -1

