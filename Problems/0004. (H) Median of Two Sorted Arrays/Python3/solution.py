class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # merge into 1 array

    m, n = len(nums1), len(nums2)
    merged = []

    i, j = 0, 0
    while i < m and j < n:
      if nums1[i] < nums2[j]:
        merged.append(nums1[i])
        i += 1
      else:
        merged.append(nums2[j])
        j += 1

    if i < m:
      merged.extend(nums1[i:])
    else:
      merged.extend(nums2[j:])
      
    tot = m + n
    if tot % 2 != 0:
      return merged[tot//2]
    else:
      return (merged[tot//2]+merged[tot//2-1])/2

