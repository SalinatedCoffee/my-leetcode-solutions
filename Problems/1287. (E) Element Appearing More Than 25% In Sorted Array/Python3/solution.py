class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    # brute force using dictionaries

    tgt = len(arr) / 4
    ints = Counter(arr)
    for k, v in ints.items():
      if v > tgt:
        return k

    return -1

