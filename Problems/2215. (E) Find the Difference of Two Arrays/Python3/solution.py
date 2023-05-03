class Solution:
  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    # sets
    
    s1 = set(nums1)
    s2 = set(nums2)

    ret = [[], []]
    for i in s1:
      if i not in s2:
        ret[0].append(i)
    for i in s2:
      if i not in s1:
        ret[1].append(i)
    
    return ret

