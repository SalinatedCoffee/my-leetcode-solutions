class Solution:
  def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # optimized brute force using sets

    common = set(nums1).intersection(nums2)
    return min(common) if common else -1

