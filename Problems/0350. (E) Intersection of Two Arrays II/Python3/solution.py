class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # dictionaries

    n1_freq, n2_freq = Counter(nums1), Counter(nums2)
    ret = []
    for k, v in n1_freq.items():
      if k in n2_freq:
        ret.extend([k]*min(v, n2_freq[k]))

    return ret

