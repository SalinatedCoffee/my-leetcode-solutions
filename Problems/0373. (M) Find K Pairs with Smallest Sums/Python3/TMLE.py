class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    # brute force using min heap
    heapify(pairs := [[i+j , (i, j)] for i in nums1 for j in nums2])
    return [x[1] for x in nsmallest(k, pairs)]

