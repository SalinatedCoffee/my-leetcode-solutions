class Solution:
  def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # two pointers

    m, n = len(nums1), len(nums2)
    a, b = 0, 0
    while a < m and b < n:
      if nums1[a] == nums2[b]:
        return nums1[a]
      if nums1[a] > nums2[b]:
        b += 1
      else:
        a += 1

    return -1

