class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # binary search

    m, n = len(nums1), len(nums2)
    total = m + n

    def recurse(l1, r1, l2, r2, k):
      # among values in the subarrays nums1[l1:r1+1], nums2[l2:r2+1]
      # return the kth number

      # no more values in subarray of nums1, directly return value in nums2
      if l1 > r1:
        return nums2[k - l1]
      # and vice versa
      if l2 > r2:
        return nums1[k - l2]
      
      # get index & value of midpoint of subarrays
      i1, i2 = (l1+r1)//2, (l2+r2)//2
      v1, v2 = nums1[i1], nums2[i2]

      # recurse on valid section
      if i1 + i2 < k:
        if v1 > v2:
          return recurse(l1, r1, i2+1, r2, k)
        return recurse(i1+1, r1, l2, r2, k)
      if v1 > v2:
        return recurse(l1, i1-1, l2, r2, k)
      return recurse(l1, r1, l2, i2-1, k)

    # if there are even number of elements, need two values about the center    
    if total % 2 != 0:
      return recurse(0, m-1, 0, n-1, total//2)
    return (recurse(0, m-1, 0, n-1, total//2-1) + recurse(0, m-1, 0, n-1, total//2)) / 2

