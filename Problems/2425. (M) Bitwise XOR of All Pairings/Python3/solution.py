class Solution:
  def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    # bit manipulation

    res = reduce(lambda x, y: x ^ y, nums2) if len(nums1) % 2 else 0
    res ^= reduce(lambda x, y: x ^ y, nums1) if len(nums2) % 2 else 0

    return res

