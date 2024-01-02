class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    # dictionaries

    freq = Counter(nums)
    ret = []
    while True:
      cur = []
      for k, v in freq.items():
        if v > 0:
          cur.append(k)
          freq[k] -= 1
      if cur:
        ret.append(cur)
      else:
        break

    return ret

